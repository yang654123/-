# -这是2022年软件杯 A4（遥感解译）赛道参赛作品，我们是还有谁+28013328队
本项目是一个通过深度学习技术实现对遥感图像自动解译的WEB系统，通过本系统的应用，实现目标提取、变化检测、目标检测和地物分类四大分析功能，系统架构如下图所示。

1、赛题介绍：（这个）
掌握国土资源利用和土地覆盖类型，是地理国情普查与监测的重要内容。高效获取准确、客观的土地利用情况，监测国土变化情况，可以为国家和地方提供地理国情信息决策支撑。随着遥感、传感器技术的发展，特别是多时相高分辨率遥感图像数据的普及，使我们可以足不出户，就能掌握全球任一地表的细微变化。

目前，我国遥感领域已步入了高分辨率影像的快车道，对遥感数据的分析应用服务的需求也与日俱增。传统方式对高分辨率卫星遥感图像的对特征刻画能力差且依赖人工经验工作量巨大。随着人工智能技术的兴起，特别是基于深度学习的图像识别方法获得了极大的发展，相关技术也推动了遥感领域的变革。相对于传统基于人海战术的目视解译方法，基于深度学习的遥感图像识别技术可以自动分析图像中的地物类型，在准确率和效率方面展现出极大的潜力。
2、算法简介及创新点介绍
  1、变化检测作为算法的考核项详细，其余三个官方给出了baseline：                                                                                                        
  a.变化检测：变化检测部分要求参赛者利用提供的训练数据，实现对多时相图像中的建筑变化检测。具体而言，多时相遥感图像建筑物变化检测任务是给定两张不同时间拍摄的相同位置（地理配准）的遥感图像，要求定位出其中建筑变化的区域。Aistudio:https://aistudio.baidu.com/aistudio/projectdetail/4107193                                                         
  b.地物分类：使用图像分割技术对卫星图像每个像素完成分类。  Aistudio:https://aistudio.baidu.com/aistudio/projectdetail/3792606                                           
  c.目标检测：使用目标检测技术对卫星图像中指定对象完成检测。Aistudio:https://aistudio.baidu.com/aistudio/projectdetail/3792609                                           
  d.目标提取：使用图像分割技术对卫星图像中指定对象完成分割。Aistudio:https://aistudio.baidu.com/aistudio/projectdetail/3792610                                           
  2、创新点：
  a.使用不同的数据增强技术（RandomHorizontalFlip(prob=0.5),RandomVerticalFlip(prob=0.1)，RandomSwap(prob=0.4)，RandomDistort()，RandomBlur(prob=0.4))                   
  b.自定义的归一化参数：                                                                                                                                                
  Normalize(
    mean=[0.471, 0.461, 0.463],                                                                                                                                    
    std=[0.173, 0.163, 0.160])                                                                                                                                        
  c.加大batchsize和裁块大小，滑窗步长。                                                                                                                                 
  训练阶段 batch size                                                                                                                                 
  TRAIN_BATCH_SIZE = 32                                                                                                                                 
  推理阶段 batch size                                                                                                                                 
  INFER_BATCH_SIZE = 32                                                                                                                                 
  裁块大小                                                                                                                                 
  CROP_SIZE = 512                                                                                                                                 
  模型推理阶段使用的滑窗步长                                                                                                                                 
  STRIDE = 32                                                                                                                                 
  改进算法思想：加大batchsize可以显著提升算法精度。原理是将同一批次的任务进行多次的训练，故提升算法精度。

3、项目介绍                                                                                                                                 
3.1前端介绍（包含前端的界面描述和启动描述，创意等）                                                                                                                                 
├─build
│  │                                                                                                                                                                  
│  ├─config
│  │                                                                                                                                                                   
│  ├─generate
│  │  │                                                                                                                                                                                                                                                                                                                          
│  │  └─icon                                                                                                                                                           
│  │                                                                                                                                                                   
│  │
│  ├─script                                                                                                                                                             
│  │
│  └─vite                                                                                                                                                               
│     │
│     └─plugin                                                                                                                                                         
│
├─mock                                                                                                                                                                 
│  │
│  ├─demo                                                                                                                                                               
│  │
│  └─sys                                                                                                                                                               
│
├─public                                                                                                                                                               
│   │
│   └─resource                                                                                                                                                         
│         ├─img                                                                                                                                                         
│         │
│         └─tinymce                                                                                                                                                         
│              ├─langs
│              │
│              └─skins                                                                                                                                                         
│                  │
│                  └─ui                                                                                                                                                 
│                     ├─oxide                                                                                                                                           
│                     │   │
│                     │   └─fonts                                                                                                                                       
│                     │
│                     └─oxide-dark                                                                                                                                    
│
├─src                                                                                                                                                        
│  │
│  ├─api                                                                                                                                                        
│  │  │
│  │  ├─demo                                                                                                                                                        
│  │  │   │
│  │  │   └─model                                                                                                                                                       
│  │  │       
│  │  ├─model                                                                                                                                                        
│  │  │
│  │  └─sys                                                                                                                                                        
│  │     │
│  │     └─model                                                                                                                                                       
│  │
│  ├─assets                                                                                                                                                        
│  │    ├─icons                                                                                                                                                        
│  │    ├─images                                                                                                                                                       
│  │    └─svg                                                                                                                                                        
│  │      
│  ├─components                                                                                                                                                        
│  │      ├─Scrollbar                                                                                                                                                   
│  │      ├─SimpleMenu                                                                                                                                                 
│  │      ├─StrengthMeter                                                                                                                                               
│  │      ├─Table                                                                                                                                                  
│  │      ├─Time                                                                                                                                                  
│  │      ├─Tinymce                                                                                                                                                  
│  │      ├─Transition                                                                                                                                                 
│  │      ├─Tree                                                                                                                                                  
│  │      ├─Upload                                                                                                                                                  
│  │      ├─Verify                                                                                                                                                  
│  │      └─VirtualScroll                                                                                                                                              
│  │      
│  ├─design                                                                                                                                                  
│  │    ├─ant                                                                                                                                                  
│  │    ├─transition                                                                                                                                                  
│  │    └─var                                                                                                                                                  
│  │
│  ├─directives                                                                                                                                                  
│  │      └─ripple                                                                                                                                                  
│  │
│  ├─enums                                                                                                                                                  
│  ├─hocks                                                                                                                                                  
│  │   ├─component                                                                                                                                                  
│  │   ├─core                                                                                                                                                  
│  │   ├─event                                                                                                                                                  
│  │   ├─setting                                                                                                                                                  
│  │   └─web                                                                                                                                                  
│  │
│  ├─layouts
│  │    ├─default                                                                                                                                                 
│  │    │     ├─content                                                                                                                                                 
│  │    │     ├─feature                                                                                                                                                 
│  │    │     ├─footer                                                                                                                                                 
│  │    │     ├─header                                                                                                                                                 
│  │    │     │   └─components                                                                                                                                        
│  │    │     ├─menu                                                                                                                                                 
│  │    │     ├─setting                                                                                                                                                 
│  │    │     │   └─components                                                                                                                                         
│  │    │     ├─sider                                                                                                                                                 
│  │    │     ├─tabs                                                                                                                                                 
│  │    │     │   └─components                                                                                                                                         
│  │    │     └─trigger                                                                                                                                                 
│  │    │
│  │    ├─iframe                                                                                                                                                 
│  │    └─page                                                                                                                                                 
│  │      
│  ├─locales                                                                                                                                                 
│  │    └─lang                                                                                                                                                 
│  │        ├─en                                                                                                                                                 
│  │        └─zh-CN                                                                                                                                                 
│  │  
│  ├─logics                                                                                                                                                 
│  │    ├─error-handle                                                                                                                                                 
│  │    ├─mitt                                                                                                                                                 
│  │    └─theme                                                                                                                                                 
│  │
│  ├─router                                                                                                                                                 
│  │    ├─guard                                                                                                                                                 
│  │    ├─helper                                                                                                                                                 
│  │    ├─menus                                                                                                                                                 
│  │    └─routes                                                                                                                                                 
│  │        └─modules                                                                                                                                                 
│  │
│  ├─settings                                                                                                                                                 
│  ├─store                                                                                                                                                 
│  │   └─modules                                                                                                                                                 
│  │
│  ├─utils                                                                                                                                                 
│  │   ├─auth                                                                                                                                                 
│  │   ├─cache
│  │   ├─event
│  │   ├─factory
│  │   ├─file
│  │   ├─helper
│  │   ├─http
│  │   │  └─axios
│  │   │
│  │   └─lib
│  │
│  └─views
│       ├─dashboard
│       │     ├─analysis
│       │     │     └─components
│       │     │         
│       │     └─workbench
│       │           └─components
│       │       
│       ├─demo
│       │   └─main-out
│       │  
│       └─sys
│          ├─about
│          ├─error-log
│          ├─exception
│          ├─iframe
│          ├─lock
│          ├─login
│          └─redirect
│
│
├─tests
│   └─server
│       ├─controller
│       └─service
│  
└─types
前端界面：
首先进入网站时会进入初始登录界面，登录界面左侧会显示log，而右侧则是登录框。登录框由用户名和密码栏以及“登录”键和“注册”键构成。                                               
当输入正确的用户名以及密码并点击“登录”键时，可以进入主功能界面；而点击“注册”，右侧的登录框则会转变成注册框，可以通过在三个输入栏中分别输入用户名，姓名，密码完成注册。
主功能界面的初始界面为目标检测界面。主功能界面由两部分组成，左侧为蓝色的选择栏，可以通过点击更换四种功能；而右侧则为具体功能界面。                                          
具体功能大致由输入图像展示，输出图像展示以及上传图片、导出图片功能构成。

3.2后端介绍（包含前后端组合，包含后端的模型部署，api调用，文件简介）
F:.
│  .env                                                                                                                                                           
│  .flaskenv                                                                                                                                                           
│  .gitignore                                                                                                                                                           
│  config.py                                                                                                                                                           
│  favicon.ico                                                                                                                                                         
│  mysqlite.db                                                                                                                                                         
│  res.json                                                                                                                                                           
│  utils.py                                                                                                                                                           
│  wsgi.py        //启动文件                                                                                                                                                           
│
├─.idea                                                                                                                                                           
│  │  .gitignore                                                                                                                                                      
│  │  misc.xml                                                                                                                                                        
│  │  modules.xml                                                                                                                                                      
│  │  MyflaskProj.iml
│  │  vcs.xml                                                                                                                                                           
│  │
│  └─inspectionProfiles                                                                                                                                                 
│          profiles_settings.xml                                                                                                                                       
│
├─app                                                                                                                                                           
│  │  __init__.py                                                                                                                                                       
│  │
│  ├─Controller                                                                                                                                                         
│  │      errors.py                                                                                                                                                     
│  │      routes.py    //前后端链接                                                                                                                                                           
│  │      user.py      //用户后端，将前端获取的注册用户信息，存取到数据库中。同时，负责登录核对数据库信息，确认是否成功登录。                                                                                                                                                           
│  │      __init__.py                                                                                                                                                           
│  │
│  └─Model                                                                                                                                                           
│          models.py                                                                                                                                                               
│          __init__.py                                                                                                                                                           
│
└─PaddleRS             //模型预测配置文件。                                                                                                                                                           
主要功能如下：                                                                                                                                                        
	登录功能                                                                                                                                                             
用户输入对于用户名和密码，点击登录，验证成功后进行登录。
	注册功能                                                                                                                                                                                                                                                                                                                     
用户输入用户名和密码，再次确认密码验证无误后，点击提交进行注册。                                                                                                                                                        
	目标提取功能                                                                                                                                                             
实现对上传的对应卫星图像的指定对象的提取。                                                                                                                                                        
	变化检测功能                                                                                                                                                             
实现了对输入两张不同时间拍摄的相同位置（地理配准）的遥感图像建筑变化的区域的定位。                                                                                                                                                        
	目标检测功能                                                                                                                                                             
实现了对输入的遥感图像指定的对象的检测出图像。                                                                                                                                                        
	地物分类功能                                                                                                                                                                                                                                                                                                                 
实现了对输入的遥感图像中感兴趣的类别的提取和分类                                                                                                                                                                                                                                                                                
3.3启动部署
后端：                                                                                                                                                        
首先需要将存有静态model文件的static文件从百度云下载好并部署到wsgi.py同级文件目录下里
静态model文件链接：https://pan.baidu.com/s/1AvwG8Rp4MWlVnWp3Uod4oQ 
提取码：epbi 
下面是启动步骤：
cd ./项目地址                                                                                                                                                         
cd ./PaddleRS                                                                                                                                                        
pip install -r requirements.txt
cd ..                                                                                                                                                        
pip install -r requirements.txt
python wsgi.py                                                                                                                                                                                                                                                                                                                     

前端：                                                                                                                                                                                                                                                                                                          
需要配置nodejs其中node版本在14以上
node install -g pnpm                                                                                                                                                        
pnpm install                                                                                                                                                                                                                                                                                                                 
pnpm serve                                                                                                                                                        

4，服务器部署                                                                                                                                                        

5.演示视频                                                                                                                                                        
https://www.bilibili.com/video/BV1sG411p7Z6?spm_id_from=333.999.0.0&vd_source=287f65f01263ba8009b98a3c108ed4a1                                                          
6.aistudio项目部署                                                                                                                                                     
https://aistudio.baidu.com/aistudio/projectdetail/4321601
