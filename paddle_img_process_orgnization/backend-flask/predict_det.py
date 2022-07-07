import paddlers as pdrs
import argparse
import cv2
import  json
import numpy as np
import copy

def py_cpu_nms(dets, thresh): #非极大值抑制    必须是整数
    # breakpoint
    dets=np.array(dets)

    x1 = dets[:, 0]
    y1 = dets[:, 1]
    x2 = dets[:, 2]
    y2 = dets[:, 3]
    areas = (y2 - y1 + 1) * (x2 - x1 + 1)
    scores = dets[:, 4]
    keep = []
    
    index = scores.argsort()[::-1]

    while index.size > 0:

        i = index[0]  # every time the first is the biggst, and add it directly
        keep.append(i)

        x11 = np.maximum(x1[i], x1[index[1:]])  # calculate the points of overlap
        y11 = np.maximum(y1[i], y1[index[1:]])
        x22 = np.minimum(x2[i], x2[index[1:]])
        y22 = np.minimum(y2[i], y2[index[1:]])

        w = np.maximum(0, x11 - x22 + 1)  # the weights of overlap
        h = np.maximum(0, y11 - y22 + 1)  # the height of overlap

        overlaps = w * h

        ious = overlaps / (areas[i] + areas[index[1:]] - overlaps)

        idx = np.where(ious <= thresh)[0]
        index = index[idx + 1]  # because index start from 1

    return keep



#static\pic_data\playground_189.jpg

def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--img_dir', '-m', type=str, default='static\pic_data\playground_189.jpg', help='model directory path')
    parser.add_argument('--thresh', '-t', type=float, default=0.2, help='threshold')
    return parser
if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    predictor = pdrs.deploy.Predictor('static/check_object')
    result = predictor.predict(img_file=args.img_dir)

    out=[]
    bboxs = []
    img = cv2.imread(args.img_dir)

    for i in range(len(result)):
        if result[i]['score']>args.thresh:
            
            out.append(result[i])#筛掉分数不高的
            temp=copy.deepcopy(result[i]['bbox'])
            temp.append(result[i]['score'])
            bboxs.append(temp)
            # bboxs.append(result[i]['bbox'])
            # bboxs.append(result[i]['score'])
            area_baifenbi=(result[i]['bbox'][2]*result[i]['bbox'][3])/(img.shape[1]*img.shape[2])

            result[i].setdefault('area',area_baifenbi)
            with open("res.json", 'a', encoding='utf-8') as fw:
                json.dump(result[i], fw, indent=4, ensure_ascii=False)
    
    # bboxs=np.array(bboxs)
    
    tmp=py_cpu_nms(bboxs,0.7)
    for i in tmp:

        cv2.rectangle(img,(int(bboxs[i][0]), int(bboxs[i][1])), (int(bboxs[i][0])+int(bboxs[i][2]), int(bboxs[i][1])+int(bboxs[i][3])), (255,0,255),2)
        cv2.putText(img,'playground',(int(bboxs[i][0]), int(bboxs[i][1])),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,0,255))


    cv2.imwrite("static/done_data/01.png",img)
    # cv2.waitKey()


