# 뚝섬에서 반포까지 


## Approach

- Jetson 보드를 살 돈이 없다 (때마침 Rpi 4B 2G model, Rpi 4B 4G model, pi camera 2 개가 나한테 있다.)
- Deep Learning 으로 자율주행을 풀어가기에는, rpi 에서는 너무 무겁다.
- 아주 Basic 한 주행을 하는 것에 꼭 Deep Learning Model 이 필요하다고 생각하지는 않는다.
- 최대한 영상처리로 돌리고, 꼭 필요한 경우 Jetson 이나 외장 TPU 등과 함께 Deep Learning 모델을 올리는 방향으로 가는 것이 좋겠다.

<br>

## Characteristic

- 속도가 빠르지 않다.
- 전원 공급이 어렵지 않지만, 적절한 전력 소비가 요구된다.
- 모빌리티에 특정 기기를 장착할 시 굉장히 많이 흔들린다.
- 한강변 자전거도로의 경우, 중앙분리선 및 자전거도로 경계선이 굉장히 명확하다.
- 차선변경 및 추월의 필요가 적다.

<br>

# Tool

## Env

- Raspberry pi B4, 2GB RAM
- Raspberry pi Camera module x 2
- (Canceled) Arducam Raspberry pi Camera hat
- Google Coral TPU
- (selection) LCD Camera
- (selection) infrared radiation Camera module x 2

<br>

### Installation

<br>

### Roadmap

- (optional) 듀얼 카메라 가능한지 공부해 보기 *내가 가지고있는 것은 single camera 인데*
- (optional) 카메라 detph mapping 하기
- 카메라 캘리브레이션하기
- 이미지 OIS 적용하기
- (selection) LCD Display 연결하기
- (selection) 적외선 Camera 에도 시도해보기


<br>

## Library

- vidstab
- opencv

<br>

# Reference

<br>

## 1. About Camera / Monitor

### 1-1. About Calibration

- 카메라 캘리브레이션이란 : https://darkpgmr.tistory.com/153
- 호모그래피 좌표계란 : https://darkpgmr.tistory.com/153
- 스테레오 정합이란 : https://m.blog.naver.com/PostView.nhn?blogId=dldlsrb45&logNo=220879295400&proxyReferer=https:%2F%2Fwww.google.com%2F

<br>

### 1-2. About Stabiliation

#### 1-2-1. H/W Solution

- 나날이 늘어가는 모바일의 OIS 도 하드웨어 없이는 안 됨. 단순히 소프트웨어 처리만 한 것이 아님.
- 짐벌을 구매하는 것이 가장 현명

<br>

#### 1-2-2. S/W Solution

- Stabilization Algorithm

<br>

### 1-3. About Dual Camera

- Multiple Camera with the RPi4 : https://www.pyimagesearch.com/2016/01/18/multiple-cameras-with-the-raspberry-pi-and-opencv/
- Stereo Camera hat 이라는 것이 있음 : https://www.arducam.com/product/b0195-synchronized-stereo-camera-hat-raspberry-pi/

> For a long time, advanced users of the Raspberry Pi community want to take video or images from multiple cameras simultaneously for 3D vids & pics, face/object detection, stereo robotic vision or advanced surveillance and live-streaming applications, so they want a real stereo camera for raspberry pi 3, 4, and other standard Pi boards. It was an unresolved problem limited by the RPi’s hardware design because the standard Raspberry pi models only have one camera port. Although Arducam has multi-camera adapter boards that let you connect up to 4 cameras to a single pi board, it only actives one camera at a time, and you have to switch between them. The other alternative is to use network-based synchronization, but you still have to use one Raspberry pi board for each camera setup, and the capture process is still not at the exact same time which will introduce the movement or artifacts between multiple images.

- Stereo Camera hat 구매처 : [가격이 8만원..](https://vctec.co.kr/product/%EC%95%84%EB%91%90%EC%BA%A0-%EC%8A%A4%ED%85%8C%EB%A0%88%EC%98%A4-%EC%8B%B1%ED%81%AC-%EC%B9%B4%EB%A9%94%EB%9D%BC-hat-%EB%9D%BC%EC%A6%88%EB%B2%A0%EB%A6%AC%EC%9A%A9-arducam-synchronized-stereo-camera-hat-for-r/16639/)

<br>

#### 1-3-1. About Depth with Dual Camera

- Example for Camera Calibration with Dual Camera + Depth Mapping with Real time : https://youtu.be/eBZm40z7E8Y
  - Guide : https://www.arducam.com/docs/cameras-for-raspberry-pi/synchronized-stereo-camera-hat/opencv-and-depth-map-on-arducam-stereo-camera-hat-tutorial/
    - Guide's Credit : https://medium.com/stereopi/opencv-and-depth-map-on-stereopi-tutorial-62cb6792bbed
    - COMPARING THE SPEED OF C++ AND PYTHON CODE ON THE RASPBERRY PI : https://stereopi.com/blog/opencv-comparing-speed-c-and-python-code-raspberry-pi-stereo-vision
    
      > We decided to measure the actual speed difference and find the performance 'bottleneck'. ... Conclusion : Python is not worse than C++. In most of the considered examples, C++ code is much faster, but in the key task – calculating depth maps from video – the performance of both solutions is the same.
      
      > The binary code for calculating depth maps does not implement multithreading, therefore, approximately one and a half cores out of four are used in the process.
      
  - Source Code : https://github.com/erget/StereoVision

<br>

### 1-4. About Display

- [LCD 후보](http://www.11st.co.kr/product/SellerProductDetail.tmall?method=getSellerProductDetail&prdNo=1953092467&gclid=CjwKCAjwztL2BRATEiwAvnALcs0lYERT7KWWM5maC-BDRbgo3wr_3f1EPVtY3SYv8ehh2SMccfOWcRoCWzAQAvD_BwE&utm_term=&utm_campaign=%B1%B8%B1%DB%BC%EE%C7%CEPC+%C3%DF%B0%A1%C0%DB%BE%F7&utm_source=%B1%B8%B1%DB_PC_S_%BC%EE%C7%CE&utm_medium=%B0%CB%BB%F6)
- [예쁜데 얘 하면 카메라 덮개 장착 가능?](https://www.cytron.io/p-5-inches-tft-touch-screen-for-rpi3-and-rpi4b)

<br>


<br>

## About Lane Fitting

- Curved Line Detection with Code (with Sliding window approach) : https://www.hackster.io/kemfic/curved-lane-detection-34f771
- About Bird's Eye View OpenCV : https://nikolasent.github.io/opencv/2017/05/07/Bird's-Eye-View-Transformation.html
- 비슷한 프로젝트 전반에 걸쳐 : https://blog.naver.com/PostView.nhn?blogId=hirit808&logNo=221486800161&redirect=Dlog&widgetTypeCall=true&directAccess=false

- Canny edge 와 Sobel edge detection 비교 : https://blog.naver.com/windowsub0406/220541314882
> Canny 는 Gaussian 이후, Sobel 을 적용하고, 가는 엣지를 가지기 위한 Convolution 연산, 그리고 엣지 연결 기법까지 들어감. 굉장히 무거운 연산일 것이라고 생각이 들어서, 그냥 Sobel 로 처리해야 할지 Canny 를 들어야 할지 

> HSV Colo Space 는 색상, 채도, 명도로 색을 구분하므로 날씨와 그림자에 따라서 Lane Detection 의 성능이 크게 달라지는 제약을 어느정도 해결 가능하다.(어두운 날씨나, 그림자와 같은)

<br>

## About Deep Learning for Object Detection Problem

<br>

### Google Coral Tpu

- 객체인식 = 라즈베리파이 + Coral EdgeTPU (이게 제일 잘되는듯) : https://blog.xcoda.net/103
- 구글 코랄(Google Coral Series) 3편, opencv 설치 카메라 테스트 : https://m.blog.naver.com/roboholic84/221861998537
- (나중에 잘 되면) 구글 코랄(Google Coral Series) 4편, web 기반의 스트리밍 해보기 : https://m.blog.naver.com/roboholic84/221868460335 
- 구글 코랄(Google Coral Series) 5편, 텍스트 그리고 스트리밍 해보기 : https://m.blog.naver.com/roboholic84/221872397487
- How to Use the Coral USB Accelerator with the Raspberry Pi :  https://www.youtube.com/watch?v=qJMwNHQNOVU
> 보니까 google coral 에 쉽게 올릴 수 있도록 제공하나봄. 이를 이용할지 직접 만들지는 선택할 것.
- Getting started with Google Coral’s TPU USB Accelerator : https://www.pyimagesearch.com/2019/04/22/getting-started-with-google-corals-tpu-usb-accelerator/
- coral 공식 문서 : https://coral.ai/docs/accelerator/get-started#on-mac

<br>

### Datasets

- Cyclist Dataset : http://www.lookingatpeople.com/download-tsinghua-daimler-cyclist/index.html
> "pedestrian", "cyclist", "motorcyclist", "tricyclist", "wheelchairuser", "mopedrider"

<br>

### Algorithms

- Part 2 - How to Run TensorFlow Lite Object Detection Models on the Raspberry Pi (with Optional Coral USB Accelerator) : https://github.com/EdjeElectronics/TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi/blob/master/Raspberry_Pi_Guide.md
- yolo v4 tensorflow light implementation : https://github.com/hunglc007/tensorflow-yolov4-tflite
> 이게 잘 돌아가는 게 최선이긴 함.

- yolo v3 tensorflow implementation : https://github.com/zzh8829/yolov3-tf2/blob/master/yolov3_tf2/models.py
> 만약 정 안되겠다 싶으면, 직접 손수 최적화시켜줘야 할수도 있으니까. 메모

<br>

### Tensorflow Lite

#### Tensorflow Lite 공식 홈페이지 : https://www.tensorflow.org/lite

Embedded Linux is an important platform for deploying machine learning. To get started using Python to perform inference with your TensorFlow Lite models, follow the Python quickstart.To instead install the C++ library, see the build instructions for Raspberry Pi or Arm64-based boards (for boards such as Odroid C2, Pine64, and NanoPi). https://www.tensorflow.org/lite/guide/get_started#linux 
- This page shows how to compile only the C++ static library for TensorFlow Lite. Alternative install options include: 
  > 그러니까 이걸 보면, tensorflow python api 를 깔 수는 있는데, LITE 만 설치하면 lite 에서 지원하는 함수들만 사용 가능하다는 이야기를 하는 듯함. 우리는 lite 버전을 설치해야 함. 또는 바로 아래, inferencing only interpreter 만 설치하면 됨.
  - **install just the Python interpreter API (for inferencing only); For more details about the Interpreter API, read Load and run a model in Python.**
    - This page shows how you can start running TensorFlow Lite models with Python in just a few minutes. All you need is a TensorFlow model [converted to TensorFlow Lite.](https://www.tensorflow.org/lite/convert/) (If you don't have a model converted yet, you can experiment using the model provided with the example linked below.)
    - If you have a Raspberry Pi, try the classify_picamera.py example to perform image classification with the Pi Camera and TensorFlow Lite.
    - If you're using a Coral ML accelerator, check out the Coral examples on GitHub.
  - install the full TensorFlow package from pip;
  - or build the full TensorFlow package.
- **how to compile only the C++ static library for TensorFlow Lite?**
  - Important concepts : TensorFlow Lite inference typically follows the following steps:
    > Train a custom model : If you have designed and trained your own TensorFlow model, or you have trained a model obtained from another source, you must convert it to the TensorFlow Lite format.
    - Loading a model : You must load the .tflite model into memory, which contains the model's execution graph.
      > To use a model with TensorFlow Lite, you must convert a full TensorFlow model into the TensorFlow Lite format — you cannot create or train a model using TensorFlow Lite. So you must start with a regular TensorFlow model, and then convert the model. **Note: TensorFlow Lite supports a limited subset of TensorFlow operations, so not all models can be converted. For details, read about the TensorFlow Lite operator compatibility.**
      > https://www.tensorflow.org/lite/guide/get_started#tensorflow_lite_converter : You can convert TensorFlow 2.0 models in a similar way. The converter can also be used from the command line, but the **Python API** (python 함수를 이용해서 파일을 convert 하는 방법) is recommended.
    - Transforming data : Raw input data for the model generally does not match the input data format expected by the model. For example, you might need to resize an image or change the image format to be compatible with the model.
      > TensorFlow Lite interpreter : The TensorFlow Lite interpreter is a library that takes a model file, executes the operations it defines on input data, and provides access to the output. The interpreter works across multiple platforms and provides a simple API for running TensorFlow Lite models from Java, Swift, Objective-C, C++, and Python.
      - [Install just the TensorFlow Lite interpreter] (https://www.tensorflow.org/lite/guide/python#install_just_the_tensorflow_lite_interpreter) : 이건 기존 tensorflow full package 에도 들어있는데, ```tf.lite.Interpreter``` 만 빼가지고 설치하는 것이라고 생각하면 됨.
        > To quickly run TensorFlow Lite models with Python, you can install just the TensorFlow Lite interpreter, instead of all TensorFlow packages.This interpreter-only package is a fraction the size of the full TensorFlow package and includes the bare minimum code required to run inferences with TensorFlow Lite—it includes only the tf.lite.Interpreter Python class. This small package is ideal when all you want to do is execute .tflite models and avoid wasting disk space with the large TensorFlow library.
      - 
    - Running inference : This step involves using the TensorFlow Lite API to execute the model. It involves a few steps such as building the interpreter, and allocating tensors, as described in the following sections.
    - Interpreting output : When you receive results from the model inference, you must interpret the tensors in a meaningful way that's useful in your application. For example, a model might return only a list of probabilities. It's up to you to map the probabilities to relevant categories and present it to your end-user.



<br>


<br>
 
<br>

> 
> 
>   - 
> 




<br>

- Keras 모델을 TensorFlow Lite로 변환하기 : https://pythonkim.tistory.com/142
> 엥 이게 이렇게 간단하다고..?
- Keras 모델을 TensorFlow Lite로 변환하기 (h5 -> pb -> tflite) : http://blog.naver.com/PostView.nhn?blogId=hhj732&logNo=221691367093


<br>

## Library Reference

- how to insert GUI to picamera monitor : https://raspberrypi.stackexchange.com/questions/78059/is-there-a-python-picam-gui-out-there
- how to install vidstab : https://pypi.org/project/vidstab/
- how to use vidstab : https://adamspannbauer.github.io/python_video_stab/html/usage.html#working-with-live-video
- how to save video file with opencv : https://www.learnopencv.com/read-write-and-display-a-video-using-opencv-cpp-python/

<br>

## Paper Reference

<br>

## Optimization Reference

- python 은 어떻게 동작하는가 : https://cjh5414.github.io/about-python-and-how-python-works/
> 박기호교수님이 컴파일러 수준에서의 최적화에 대해서 이야기를 했는데, python 도 최적화가 가능한가에 대해서 의문을 가지고 찾아보게 됨. 어느 레벨에서 돌아가는 것인지. 검색 결과, 우리가 python 코드를 작성하고 실행하면 C 로 작성된 ```CPython``` 이 python 코드를 바이너리 코드로 바꾸어 주고, 그 바이너리 코드를 한줄씩 읽어주는 것도 그 ```CPython``` 이라고 한다. 즉, 컴파일러이면서 인터프리터 역할도 하는 것. python 코드를 C언어로 바꾸는 것이 아니라 컴파일하여 bytecode로 바꾸고 그 다음에 ```CPython``` interpreter(virtual machine)가 실행하는 것. ```.py``` 파일을 실행하면 ```.pyc``` 라는 파일이 생성되는데 이것이 ```CPython```이 컴파일한 bytecode가 들어있는 것이다. 그 다음 ```.pyc```를 interpret 하는 것도 CPyton이다.
- Why python is slow? : http://jakevdp.github.io/blog/2014/05/09/why-python-is-slow/
> 모두 이해할 여유는 없어 앞부분만 간단히 읽어보았을 때, python 의 가변 데이터 타입때문에, 그것을 구현하는 C의 구조체가 열일을 한다. 정도로 이해했다. 최대한 python 변수의 수를 줄이고, 같은 변수이더라도 이를 정적 데이터 타입인 numpy 나, 이미 컴파일되어 배포되는 opencv 같이 최적화가 이미 완료된 라이브러리들을 이용하는 것이 좋은 방법일 것 같다는 생각이 든다.
- Raspberry pi 를 위한 Google Edge TPU : https://blog.xcoda.net/103
> SSD MobileNet Version 이 8~10FPS 정도가 나온다고 하니 꽤나 준수하다.

<br>

## Legacy (not used)

- Single Camera Calibration : https://youtu.be/QV1a1G4lL3U
- Getting Started with LAIDAR Arduino : https://youtu.be/VhbFbxyOI1k
- 왜 OpenCV 는 RGB 가 아니라 BGR Format 을 쓸까 : https://blog.xcoda.net/102?category=586774

<br>
