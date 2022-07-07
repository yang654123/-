from __future__ import print_function
import base64
import os
from flask import Blueprint, jsonify
from flask import render_template, flash, redirect, url_for, request,session
from sqlalchemy import func
from config import Config
from PIL import Image
from app import db
from app.Model.models import User
from paddlers.deploy import Predictor
from matplotlib import pyplot as plt
import cv2
import paddlers as pdrs
import argparse
import cv2
import  json
import numpy as np

bp_routes = Blueprint('routes', __name__)
bp_routes.template_folder = Config.TEMPLATE_FOLDER #'..\\View\\templates'

UPLOAD_FOLDER = 'static/pic_data'
DOWNLOAD_FOLDER = 'static/done_data'
TARGET_NUM = 0

@bp_routes.route('/upload_target_detection_img/', methods=['GET','POST'])
def upload_target_detection_img():
    if request.method == 'POST':
        # predictor = Predictor("static/check_object")
        # res = predictor.predict("static/pic_data/A.png")
        # cm_1024x1024 = res['label_map']
        # img = (cm_1024x1024 * 255).astype('uint8')
        # cv2.imwrite("static/done_data/03.png", img)
        img1 = request.files['TargetDetection']
        target_detection_img = Image.open(img1.stream)
        # 保存图片
        target_detection_img.save('TargetDetection.png')   #target_detection_img.save('TargetDetection.png')
        
        thresh=0.2
        predictor = pdrs.deploy.Predictor('static/check_object')
        img_file="TargetDetection.png"
        result = predictor.predict(img_file="TargetDetection.png")
        # print(result[:, 0])
        out=[]
        bboxs = []
        img = cv2.imread(img_file)
        # print(result)
        # result=py_cpu_nms(result,0.02)
        for i in range(len(result)):
            if result[i]['score']>thresh:
                print(i)
                out.append(result[i])#筛掉分数不高的
                bboxs.append(result[i]['bbox'])
                area_baifenbi=(result[i]['bbox'][2]*result[i]['bbox'][3])/(img.shape[1]*img.shape[2])
                print(area_baifenbi)
                result[i].setdefault('area',area_baifenbi)
                with open("res.json", 'a', encoding='utf-8') as fw:
                    json.dump(result[i], fw, indent=4, ensure_ascii=False)
        print(bboxs)


        for i in range(len(bboxs)):
            cv2.rectangle(img,(int(bboxs[i][0]), int(bboxs[i][1])), (int(bboxs[i][0])+int(bboxs[i][2]), int(bboxs[i][1])+int(bboxs[i][3])), (255,0,255),2)
            cv2.putText(img,'playground',(int(bboxs[i][0]), int(bboxs[i][1])),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,0,255))


        cv2.imwrite("static/done_data/01.png",img)
        # cv2.waitKey()

        img_stream = ''
        target_path = 'static/done_data/01.png'
        # 图像变换后更改target_path路径即可
        with open(target_path,'rb') as img_f:
            img_stream = img_f.read()
            img_stream = base64.b64encode(img_stream).decode()
        
        # 获取图像后移除源图像文件
        # os.remove(target_path)

        rsp={
            "code":0,
            'img_stream':'data:image/png;base64,'+img_stream,
            }
        return jsonify(rsp)


@bp_routes.route('/upload_classification_features_img/', methods=['GET','POST'])
def upload_classification_features_img():
    if request.method == 'POST':
        img = request.files['ClassificationofFeatures']
        classification_features_img = Image.open(img.stream)
        # 保存图片
        classification_features_img.save('ClassificationofFeatures.png')
        
        predictor = Predictor("static/object_classification")
        res = predictor.predict("ClassificationofFeatures.png")
        cm_1024x1024 = res['label_map']
        # print(res)
        img = (cm_1024x1024 * 255).astype('uint8')
        file_name="static/done_data/03.png"
        cv2.imwrite(file_name, img)
        img_stream = ''
        target_path = file_name
        # 图像变换后更改target_path路径即可
        with open(target_path,'rb') as img_f:
            img_stream = img_f.read()
            img_stream = base64.b64encode(img_stream).decode()
        # 获取图像后移除源图像文件
        # os.remove(target_path)
        rsp={
            "code":0,
            'img_stream':'data:image/png;base64,'+img_stream,
            }
        return jsonify(rsp) 


@bp_routes.route('/upload_target_extraction_img/', methods=['GET','POST'])
def upload_target_extraction_img():
    if request.method == 'POST':
        img = request.files['TargetExtraction']
        target_extraction_img = Image.open(img.stream)
        # 保存图片
        target_extraction_img.save('TargetExtraction.png')
        

        predictor = Predictor("static/get_object",use_gpu=True)
        res = predictor.predict(img_file='TargetExtraction.png')
        # print(res)
        cm_1024x1024 = res['label_map']
        #print(np.max(cm_1024x1024))
        img1 = (cm_1024x1024*255).astype('uint8')
        file_name="static/done_data/04.png"
        cv2.imwrite(file_name, img1)

        img_stream = ''
        target_path = file_name
        # 图像变换后更改target_path路径即可
        # 图像变换后更改target_path路径即可

        with open(target_path,'rb') as img_f:
            img_stream = img_f.read()
            img_stream = base64.b64encode(img_stream).decode()
        
        # 获取图像后移除源图像文件
        # os.remove(target_path)

        rsp={
            "code":0,
            'img_stream':'data:image/png;base64,'+img_stream,
            }
        return jsonify(rsp)

        # with open(target_path,'rb') as img_f:
        #     img_stream = img_f.read()
        #     img_stream = base64.b64encode(img_stream).decode()
        
        # # 获取图像后移除源图像文件
        # # os.remove(target_path)
        # rsp={
        #     "code":0,
        #     'img_stream':'data:image/png;base64,'+img_stream,
        #     }
        # return jsonify(rsp) 



@bp_routes.route('/upload_change_detection_img1/', methods=['GET','POST'])
def upload_change_detection_img1():
    if request.method == 'POST':
        img = request.files['ChangeDetection1']
        target_detection_img = Image.open(img.stream)
        # 保存图片
        target_detection_img.save('ChangeDetection1.png')
        
        # img_stream = ''
        target_path = 'ChangeDetection1.png'
        # 图像变换后更改target_path路径即可
        with open(target_path,'rb') as img_f:
            img_stream = img_f.read()
            img_stream = base64.b64encode(img_stream).decode()
        
        # 获取图像后移除源图像文件
        # os.remove(target_path)

        rsp={
            "code":0,
            'img_stream':'data:image/png;base64,'+img_stream,
            }
        return jsonify(rsp) 

@bp_routes.route('/upload_change_detection_img2/', methods=['GET','POST'])
def upload_change_detection_img2():
    if request.method == 'POST':
        img = request.files['ChangeDetection2']
        target_detection_img = Image.open(img.stream)
        # 保存图片
        target_detection_img.save('ChangeDetection2.png')
        
        img_stream = ''
        target_path = 'ChangeDetection2.png'
        # 图像变换后更改target_path路径即可
        with open(target_path,'rb') as img_f:
            img_stream = img_f.read()
            img_stream = base64.b64encode(img_stream).decode()
        
        # 获取图像后移除源图像文件
        # os.remove(target_path)

        rsp={
            "code":0,
            'img_stream':'data:image/png;base64,'+img_stream,
            }
        return jsonify(rsp) 


@bp_routes.route('/change_detection/', methods=['GET','POST'])
def change_detection():
    if request.method == 'POST':

        predictor = Predictor("static/1024")
        res = predictor.predict(("ChangeDetection1.png", "ChangeDetection2.png"))
        res=res[0]
        print(res)
        cm_1024x1024 = res['label_map']
        img = (cm_1024x1024 * 255).astype('uint8')
        print("变化检测")
        # filename = '01.png'
        # filepath = os.path.join(DOWNLOAD_FOLDER, filename)
        filepath = 'static/done_data/02.png'
        cv2.imwrite(filepath, img)
        
        
        target_path = filepath
        # 图像变换后更改target_path路径即可
        with open(target_path,'rb') as img_f:
            img_stream = img_f.read()
            img_stream = base64.b64encode(img_stream).decode()
        
        # 获取图像后移除源图像文件
        # os.remove(target_path)

        rsp={
            "code":0,
            'img_stream':'data:image/png;base64,'+img_stream,
            }
        return jsonify(rsp) 



