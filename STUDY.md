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

<br>

### Installation

<br>

### Roadmap

- 듀얼 카메라 가능한지 공부해 보기 *내가 가지고있는 것은 single camera 인데*
- 듀얼 카메라 캘리브레이션하기
- 듀얼 카메라 detph mapping 하기
- depth mapping 된 이미지 + 합쳐진 이미지 OIS 적용하기
- (selection) LCD Display 연결하기
- (selection) 적외선 Camera 에도 시도해보기

<br>

## Library

- vidstab
- opencv

<br>

## Reference

<br>

- Example for Camera Calibration with Dual Camera + Depth Mapping with Real time : https://youtu.be/eBZm40z7E8Y

<br>

### Library

- how to install vidstab : https://pypi.org/project/vidstab/
- how to use vidstab : https://adamspannbauer.github.io/python_video_stab/html/usage.html#working-with-live-video

<br>

### Papers

<br>
