<template>
  <PageWrapper title="目标检测" >

    <CollapseContainer title="图像上传"  class="my-4">

      <div class="container p-6">
        <p>选择图片 </p>
        <div class="container">
              <a-image :src="previewImg" alt="" :width="300"  />
        </div>
         <p>提取结果 </p>
        <div class="container">
              <a-image :src="rspviewImg" alt="" :width="300"  />
        </div>
      </div>
    </CollapseContainer>

      <div class="upload-modal-content">
        <a-upload
          :file-list="uploadedFileList"
          :max-count="1"
          :customRequest="uploadFiles"
          :showUploadList="false"
        >
          <Button   size="middle" :loading="loading">
            上传文件
          </Button>
        </a-upload>
      </div>

  </PageWrapper>
</template>
<script lang="ts">
  import { defineComponent, ref } from 'vue';
  import { PageWrapper } from '/@/components/Page';
  import { CollapseContainer } from '/@/components/Container';
  import { CropperImage, CropperAvatar } from '/@/components/Cropper';
  import { uploadApi } from '/@/api/sys/upload';
  import img from '/@/assets/images/header.jpg';
  import { useUserStore } from '/@/store/modules/user';
  import axios from 'axios';
  import {  Button  } from 'ant-design-vue';
  export default defineComponent({
    components: {
      PageWrapper,
      CropperImage,
      CollapseContainer,
      CropperAvatar,
            Button
    },
    setup() {
      const info = ref('');
      const cropperImg = ref('');
      const circleInfo = ref('');
      const circleImg = ref('');
      const userStore = useUserStore();
      const avatar = ref(userStore.getUserInfo?.avatar || '');
            const loading = ref(false);
      function handleCropend({ imgBase64, imgInfo }) {
        info.value = imgInfo;
        cropperImg.value = imgBase64;
      }

      function handleCircleCropend({ imgBase64, imgInfo }) {
        circleInfo.value = imgInfo;
        circleImg.value = imgBase64;
      }

      const previewImg = ref('../src/assets/images/index.png');
      const rspviewImg = ref('../src/assets/images/index.png');
      const uploadedFileList = ref([]);

      
      return {
        img,
        info,
        circleInfo,
        cropperImg,
        circleImg,
        handleCropend,
        handleCircleCropend,
        avatar,
        uploadApi: uploadApi as any,
        uploadedFileList,
        previewImg,
        rspviewImg,
        loading
      };
    },

methods: {
    /******************上传文件方法******************/
      async uploadFiles(info) {
        //初始化文件信息
        const fileInfo = {
          uid: info.file.uid,
          name: info.file.name,
          status: "uploading",
          response: "",
          url: "",
        };
        //放入上传列表中，以便于显示上传进度
        this.uploadedFileList=[fileInfo];
        //开始真正上传
        //上传接口
        let uploadApiUrl = "https://localhost:3100/basic-api/upload_target_detection_img/";
        //调用公共上传方法
        this.loading = true;
        const res = await this.uploadFilesToServer(
          uploadApiUrl,
          "files[]",
          info.file
        );
        // console.log("uploadFiles-res",res)
        //根据服务端返回的结果判断成功与否，设置文件条目的状态
        if (res.code == 0) {
          this.loading = false;
          fileInfo.status = "done";
          this.rspviewImg = res.img_stream;
          // fileInfo.response = res.msg;
          // fileInfo.url = res.data[0].file;
          // console.log("uploadedFileList:",this.uploadedFileList);
        } 
        else {
          this.loading = false;
          fileInfo.status = "error";
          fileInfo.response = res.msg;
          
        }
      },

      /******************上传文件公共方法******************/
      uploadFilesToServer(uploadApiUrl, fileName, files) {
        let formData = new FormData();
        const fr = new FileReader()
        fr.readAsDataURL(files)
        fr.onload = (e) => {
          // 通过 e.target.result 获取到读取的结果，值是 BASE64 格式的字符串
          // 法1
          // this.$refs.imgRef.src = e.target.result
          // 法2
          this.previewImg = e.target.result
          // console.log("this.previewImg,",this.previewImg)
        }
      
        formData.append('TargetDetection', files);
        // console.log("formData:---,",formData)
        // 添加请求头
        const headers = {
          "Content-Type": "multipart/form-data",
        };
        //配置头
        const request = axios.create({
          headers: headers,
        });
        //开始上传
        return request
          .post(uploadApiUrl, formData)
          .then((response) => {
            // console.log("uploadFilesToServer-response",response)
            return Promise.resolve(response.data);
          })
          .catch((error) => {
            return Promise.reject(error);
          });
      },
    },

  });
</script>

<style scoped>
  .container {
    display: flex;
    width: 100vw;
    align-items: center;
  }

  .cropper-container {
    width: 40vw;
  }

  .croppered {
    height: 500px;
  }

  p {
    margin: 10px;
  }

.cover-img {
  width: 400px;
  height: 400px;
  object-fit: cover;
}


</style>
