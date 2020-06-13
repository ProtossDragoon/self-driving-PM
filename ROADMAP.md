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

