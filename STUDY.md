# 뚝섬에서 반포까지 

## Approach

- Jetson 보드를 살 돈이 없다 (때마침 Rpi 4B 2G model, Rpi 4B 4G model, pi camera 2 개가 나한테 있다.)
- Deep Learning 으로 자율주행을 풀어가기에는, rpi 에서는 너무 무겁다.
- 아주 Basic 한 주행을 하는 것에 꼭 Deep Learning Model 이 필요하다고 생각하지는 않는다.
- 최대한 영상처리로 돌리고, 꼭 필요한 경우 Jetson 과 함께 Deep Learning 모델을 올리는 방향으로 가는 것이 좋겠다.

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
- 
- (selection) LCD Display 연결하기
- (selection) 적외선 Camera 에도 시도해보기


<br>

## Library

- vidstab
- opencv

<br>

# Reference

<br>

### About Calibration

- 카메라 캘리브레이션이란 : https://darkpgmr.tistory.com/153
- 호모그래피 좌표계란 : https://darkpgmr.tistory.com/153
- 스테레오 정합이란 : https://m.blog.naver.com/PostView.nhn?blogId=dldlsrb45&logNo=220879295400&proxyReferer=https:%2F%2Fwww.google.com%2F

<br>

### About Display

- [LCD 후보](http://www.11st.co.kr/product/SellerProductDetail.tmall?method=getSellerProductDetail&prdNo=1953092467&gclid=CjwKCAjwztL2BRATEiwAvnALcs0lYERT7KWWM5maC-BDRbgo3wr_3f1EPVtY3SYv8ehh2SMccfOWcRoCWzAQAvD_BwE&utm_term=&utm_campaign=%B1%B8%B1%DB%BC%EE%C7%CEPC+%C3%DF%B0%A1%C0%DB%BE%F7&utm_source=%B1%B8%B1%DB_PC_S_%BC%EE%C7%CE&utm_medium=%B0%CB%BB%F6)
- [예쁜데 얘 하면 카메라 덮개 장착 가능?](https://www.cytron.io/p-5-inches-tft-touch-screen-for-rpi3-and-rpi4b)


<br>

### About Dual Camera

- Multiple Camera with the RPi4 : https://www.pyimagesearch.com/2016/01/18/multiple-cameras-with-the-raspberry-pi-and-opencv/
- Stereo Camera hat 이라는 것이 있음 : https://www.arducam.com/product/b0195-synchronized-stereo-camera-hat-raspberry-pi/

> For a long time, advanced users of the Raspberry Pi community want to take video or images from multiple cameras simultaneously for 3D vids & pics, face/object detection, stereo robotic vision or advanced surveillance and live-streaming applications, so they want a real stereo camera for raspberry pi 3, 4, and other standard Pi boards. It was an unresolved problem limited by the RPi’s hardware design because the standard Raspberry pi models only have one camera port. Although Arducam has multi-camera adapter boards that let you connect up to 4 cameras to a single pi board, it only actives one camera at a time, and you have to switch between them. The other alternative is to use network-based synchronization, but you still have to use one Raspberry pi board for each camera setup, and the capture process is still not at the exact same time which will introduce the movement or artifacts between multiple images.

- Stereo Camera hat 구매처 : [가격이 8만원..](https://vctec.co.kr/product/%EC%95%84%EB%91%90%EC%BA%A0-%EC%8A%A4%ED%85%8C%EB%A0%88%EC%98%A4-%EC%8B%B1%ED%81%AC-%EC%B9%B4%EB%A9%94%EB%9D%BC-hat-%EB%9D%BC%EC%A6%88%EB%B2%A0%EB%A6%AC%EC%9A%A9-arducam-synchronized-stereo-camera-hat-for-r/16639/)

<br>

**About Depth with Dual Camera** <br>
- Example for Camera Calibration with Dual Camera + Depth Mapping with Real time : https://youtu.be/eBZm40z7E8Y
  - Guide : https://www.arducam.com/docs/cameras-for-raspberry-pi/synchronized-stereo-camera-hat/opencv-and-depth-map-on-arducam-stereo-camera-hat-tutorial/
    - Guide's Credit : https://medium.com/stereopi/opencv-and-depth-map-on-stereopi-tutorial-62cb6792bbed
    - COMPARING THE SPEED OF C++ AND PYTHON CODE ON THE RASPBERRY PI : https://stereopi.com/blog/opencv-comparing-speed-c-and-python-code-raspberry-pi-stereo-vision
    
      > We decided to measure the actual speed difference and find the performance 'bottleneck'. ... Conclusion : Python is not worse than C++. In most of the considered examples, C++ code is much faster, but in the key task – calculating depth maps from video – the performance of both solutions is the same.
      
      > The binary code for calculating depth maps does not implement multithreading, therefore, approximately one and a half cores out of four are used in the process.
      
  - Source Code : https://github.com/erget/StereoVision

<br>

### About Algorithms

- Curved Line Detection with Code (with Sliding window approach) : https://www.hackster.io/kemfic/curved-lane-detection-34f771
- About Bird's Eye View OpenCV : https://nikolasent.github.io/opencv/2017/05/07/Bird's-Eye-View-Transformation.html

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
> 박기호교수님이 컴파일러 수준에서의 최적화에 대해서 이야기를 했는데, python 도 최적화가 가능한가에 대해서 의문을 가지고 찾아보게 됨. 어느 레벨에서 돌아가는 것인지.
- Why python is slow? : http://jakevdp.github.io/blog/2014/05/09/why-python-is-slow/
- Raspberry pi 를 위한 Google Edge TPU : https://blog.xcoda.net/103
> SSD MobileNet Version 이 8~10FPS 정도가 나온다고 하니 꽤나 준수하다.

<br>

## Legacy (not used)

- Single Camera Calibration : https://youtu.be/QV1a1G4lL3U
- Getting Started with LAIDAR Arduino : https://youtu.be/VhbFbxyOI1k

<br>
