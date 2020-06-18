# Roadmap

## Raspberry Pi

- [라즈베리파이 OS 설치 이미지 다운로드](https://www.raspberrypi.org/downloads/)


- [라즈베리파이 내부 고정 ip 설정](https://www.sagein.net/655)
  - [공유기 설정창](https://pastimelife.com/1554) : PASS : 2164AD_admin (*해킹하지말아주세요 ㅜㅜ*)
  - [공유기에서 고정하기](https://rottk.tistory.com/entry/%EB%9D%BC%EC%A6%88%EB%B2%A0%EB%A6%AC%ED%8C%8C%EC%9D%B4-IP-%EA%B3%A0%EC%A0%95%ED%95%98%EA%B8%B0)


- 유선으로 하면 잘 되는데 와이파이로 걸었다 하면 종종 끊기는 문제

'''
sudo rfkill list
sudo rfkill unblock
'''

<br>

### Putty and others

- 공유기 내부 ip : 192.168.35.1
- rpi 4B 4G model : 192.168.35.78, 2100번포트
- rpi 4B 2G model : 192.168.35.210, 2101번포트
- install X11
- putty + port : localhost:0
- run GUI for linux

'''
lxsession
'''

<br>

## openCV

- [설치 과정은 이 게시글을 참고함](https://make.e4ds.com/make/learn_guide_view.asp?idx=116)
- [이 게시글도 참고함](https://bluexmas.tistory.com/964)
- 임베디드시스템 박기호 교수님강의자료 참고함

<br>

```
sudo apt-get install build-essential
sudo apt-get install cmake

// 특정 포멧의 이미지 파일을 Read, Write 하기 위한 필요 패키지 설치
sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev

// 특정 코덱의 비디오 파일을 Read, Write 하기 위한 필요 패키지 설치
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libxvidcore-dev libx264-dev libxine2-dev

// Video4Linux  리눅스에서 실시간 비디오 캡처 및 비디오 디바이스 제어를 위한 API 패키지 설치
sudo apt-get install libv4l-dev v4l-utils

// GStreamer는 리눅스 기반에서 영상 스트리밍을 쉽게 처리할 수 있더록 만든 오픈 소스 프레임워크 이다.
sudo apt-get install libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev

// OpenCV에서 윈도우 생성 등의 GUI를 위해 gtk 또는 qt를 선택해서 사용가능하며 여기서는 gtk2를 지정해준다.
sudo apt-get install libgtk2.0-dev

// OpenGL 지원하기 위해 필요한 라이브러리 설치
sudo apt-get install mesa-utils libgl1-mesa-dri libgtkgl2.0-dev libgtkglext1-dev

// OpenCV 최적화를 위해 사용되는 라이브러리 설치
sudo apt-get install libatlas-base-dev gfortran libeigen3-dev

// python 패키지는 OpenCV-Python 바인딩을 위한 패키지이며, Numpy는 매트릭스 연산등을 빠르게 처리할 수 있다. 
// 물론 이미 설치되어 있음.
sudo apt-get install python3-dev python3-numpy

```

- 아 개오바다 이거 언제 다 설치하냐?


```
~/Desktop$ mkdir opencvtemp
~/Desktop$ cd opencvtemp

wget -O opencv.zip https://github.com/opencv/opencv/archive/**4.1.2.zip**
unzip opencv.zip

wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/4.1.2.zip
unzip opencv_contrib.zip


~/Desktop/opencvtemp/$ cd opencv-4.1.2
~/Desktop/opencvtemp/opencv-4.1.2$ mkdir build
~/Desktop/opencvtemp/opencv-4.1.2$ cd build

~/Desktop/opencvtemp/opencv-4.1.2/build$ 
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local  -D WITH_TBB=OFF -D WITH_IPP=OFF -D WITH_1394=OFF -D BUILD_WITH_DEBUG_INFO=OFF -D BUILD_DOCS=OFF -D INSTALL_C_EXAMPLES=ON -D INSTALL_PYTHON_EXAMPLES=ON -D BUILD_EXAMPLES=OFF -D BUILD_TESTS=OFF -D BUILD_PERF_TESTS=OFF -D ENABLE_NEON=ON -D ENABLE_VFPV3=ON -D WITH_QT=OFF -D WITH_GTK=ON -D WITH_OPENGL=ON -D OPENCV_ENABLE_NONFREE=ON -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib-4.1.2/modules -D WITH_V4L=ON -D WITH_FFMPEG=ON -D WITH_XINE=ON -D ENABLE_PRECOMPILED_HEADERS=OFF -D BUILD_NEW_PYTHON_SUPPORT=ON -D OPENCV_GENERATE_PKGCONFIG=ON ../

```

```
// 컴파일 시 메모리 부족으로 에러가 나지 않도록 swap 공간을 늘려줘야 한다.

// /etc/dphys-swapfile 파일을 연다
~/Desktop/opencvtemp/opencv-4.1.2/build $ sudo vim /etc/dphys-swapfile

// 변경
CONF_SWAPSIZE=2048

// swap을 재시작하여 변경된 설정값을 반영해준다.
sudo /etc/init.d/dphys-swapfile restart


~/Desktop/opencvtemp/opencv-4.1.2/build $ make -j4

sudo make install
sudo ldconfig
```

- 자 이제 여기까지 했으면 이제 import cv2 가 작동된다.
- CONF_SWAPSIZE를 100MB로 재설정,  스왑 서비스를 재시작

```
sudo vim /etc/dphys-swapfile
sudo /etc/init.d/dphys-swapfile restart
```

- 하지만, 이것은 전역에 설치된 것일 뿐 가상환경에 넣어줘야 함. OpenCV 4를 Python 3 가상 환경에 복사(소프트링크)
- 소프트링크 옵션 (-s)
- 원본 파일 위치 /usr/local/lib/python3.7/site-packages/cv2/python-3.7/cv2.cpython-37m-arm-linux-gnueabihf.so
- 복사할 이름 cv2.so

```
cd ~/Desktop/tfliteinter_env/lib/python3.7/site-packages
~/Desktop/tfliteinter_env/lib/python3.7/site-packages$ ln -s /usr/local/lib/python3.7/dist-packages/cv2/python-3.7/cv2.cpython-37m-arm-linux-gnueabihf.so cv2.so
```


## Coral

```
echo "deb https://packages.cloud.google.com/apt coral-edgetpu-stable main" | sudo tee /etc/apt/sources.list.d/coral-edgetpu.list

curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -

sudo apt-get update
```

- USB 가 꽂혀 있으면 우선 다시 뽑아야 함
- 이미 꽂힌 채로 아래 커맨드를 수행할 시 제거 후 재설치
- 아래 커맨드는 둘 중 하나 선택.

```
sudo apt-get install libedgetpu1-std
sudo apt-get install libedgetpu1-max
```

<br>

## Virtual Env

- [가상환경 참고](https://jamanbbo.tistory.com/45)

```
pip3 list

// python 에서 기본으로 제공하는 virtualenv

python3 -m venv ./tffull_env
python3 -m venv ./tf2_env
python3 -m venv ./tfliteinter_env
```

```
cd tffull_env
source bin/activate
pip3 list
```

<br>

### (virtualenv) install tf1.15

- tf1.15 is latest version of tensorflow
- tf1.15 만 coral 을 지원함.
- 하지만 pip 를 통한 간단한 install 을 linux 에서 지원하지 않음
- 따라서 [이 링크를 참고](https://qengineering.eu/install-tensorflow-1.15.2-on-raspberry-pi-4.html)

```
(tffull_env) sudo apt-get install libhdf5-dev libc-ares-dev libeigen3-dev
(tffull_env) sudo apt-get install libatlas-base-dev libatlas3-base
(tffull_env) pip install h5py
(tffull_env) pip install six 
(tffull_env) pip wheel mock
(tffull_env) pip wheel wheel
(tffull_env) pip install tensorflow-1.15.2-cp37-cp37m-linux_armv7l.whl
// sudo pip install 명령어 사용시, 전역에 깔려버림.
```

<br>

### (virtualenv) install tflite runtime interpreter and Run Demo

- [참고](https://www.tensorflow.org/lite/guide/python)
- [데모 참고](https://coral.ai/docs/accelerator/get-started/#3-run-a-model-using-the-tensorflow-lite-api)

```
(tfliteinter_env) pip install https://dl.google.com/coral/python/tflite_runtime-2.1.0.post1-cp37-cp37m-linux_armv7l.whl

```

```
(tfliteinter_env) mkdir coral && cd coral
(tfliteinter_env) git clone https://github.com/google-coral/tflite.git
(tfliteinter_env) cd tflite/python/examples/classification
(tfliteinter_env) bash install_requirements.sh
(tfliteinter_env) python3 classify_image.py --model models/mobilenet_v2_1.0_224_inat_bird_quant_edgetpu.tflite --labels models/inat_bird_labels.txt --input images/parrot.jpg
```

<br>

- [데모 github](https://github.com/google-coral/examples-camera)

```
(tfliteinter_env) mkdir examples-camera-original
(tfliteinter_env) cd examples-camera-original
(tfliteinter_env) cd examples-camera
(tfliteinter_env) git clone https://github.com/google-coral/examples-camera
(tfliteinter_env) sh download_models.sh
(tfliteinter_env) cd pygame
(tfliteinter_env) bash install_requirements.sh
```

만약 이렇게 했는데 pygame 이 설치가 안 된 경우, (pip list 를 통해 확인)

```
(tfliteinter_env) pip3 install pygame
```

<br>
데모 실행


```
(tfliteinter_env) python3 detect.py
```
<br>

### (virtualenv)

- [이제 CAM 을 돌려보자](https://github.com/ProtossDragoon/self-driving-PM.git

해당 repo 는 original repo 와 다르게
- resize 의 편의를 위해 window 의 모양을 정방형으로 수정함.
- 라즈베리파이 4B 에 맞춰, 카메라를 기본 연결 카메라 [0] 번 카메라로 수정함.
- setting 이 custom 폴더로 잡혀있음.



<br>

### 내가 읽어야 할 코드

https://colab.research.google.com/github/google-coral/tutorials/blob/master/retrain_classification_ptq_tf1.ipynb#scrollTo=TaX0smDP7xQY


<br>



### Dataset

- 또 그거 언제 학습시키지..
- 일단 COCO 데이터셋으로 학습된 애 가져다가 한번 인터프리터로 테스트 해보자.
- 위에 코랩 저거 소스코드에, 내가 만들었던 CAM 합쳐가지고 보여주는 게 더 이펙트있을듯.
- 그리고 그거 가져다가 CAM 소스코드 붙이자.
- 시간 남으면 자전거탄사람 뒷모습 구글에서 클롤링해다가 가져다붙이면 될듯.

<br>

### 그리고

- 멀티코어가 가능할까?
- A 프로세스에서 매 프레임마다 전역변수 읽는데, fork 된 B프로세스...

<br>

## Camera

- 캘리브레이션
  - 카메라 파라미터 구하기
  - 카메라 파라미터 적용하기

<br>

### Calibration

- [카메라 캘리브레이션, camera parameter 구하는 source code](https://nikatsanka.github.io/camera-calibration-using-opencv-and-python.html)
