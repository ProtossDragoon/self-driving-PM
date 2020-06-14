# Roadmap

## Raspberry Pi

- [라즈베리파이 OS 설치 이미지 다운로드](https://www.raspberrypi.org/downloads/)


- [라즈베리파이 내부 고정 ip 설정](https://www.sagein.net/655)
  - [공유기 설정창](https://pastimelife.com/1554) : PASS : 2164AD_admin (*해킹하지말아주세요 ㅜㅜ*)
  - [공유기에서 고정하기](https://rottk.tistory.com/entry/%EB%9D%BC%EC%A6%88%EB%B2%A0%EB%A6%AC%ED%8C%8C%EC%9D%B4-IP-%EA%B3%A0%EC%A0%95%ED%95%98%EA%B8%B0)
  - 공유기 ip : 192.168.35.1
  - rpi 4B 4G model : 192.168.35.78, 2100번포트
  - rpi 4B 2G model : 192.168.35.210, 2101번포트

<br>

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

### 내가 읽어야 할 코드

https://colab.research.google.com/github/google-coral/tutorials/blob/master/retrain_classification_ptq_tf1.ipynb#scrollTo=TaX0smDP7xQY


<br>


### Dataset

- 또 그거 언제 학습시키지..
- 일단 COCO 데이터셋으로 학습된 애 가져다가 한번 인터프리터로 테스트 해보자.
- 위에 코랩 저거 소스코드에, 내가 만들었던 CAM 합쳐가지고 보여주는 게 더 이펙트있을듯.
- 그리고 그거 가져다가 CAM 소스코드 붙이자.
- 시간 남으면 자전거탄사람 뒷모습 구글에서 클롤링해다가 가져다붙이면 될듯.


### 그리고

- 멀티코어가 가능할까?
- A 프로세스에서 매 프레임마다 전역변수 읽는데, fork 된 B프로세스...
