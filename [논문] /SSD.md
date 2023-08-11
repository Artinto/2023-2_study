# SSD (2016)
**Single Shot Multibox Detector**   
Review.LSJ, 2023.08.08   
## Abstract   
* region proposal(영역 제안) 과정을 생략하는 1-stage 모델
* 1-stage 모델임에도 불구하고 2-stage 모델인 Faster R-CNN 능가하는 정확도
* 6개의 서로다른 scale의 Multi Feature Map과 각 Feature Map의 각 cell마다 서로 다른 scale과 aspect ratio를 가진 Default Box 사용   
  > Default Box : Faster R-CNN 모델의 Anchor Box와 유사하지만 다양한 해상도를 갖는 feature map 활용
  
  > Anchor box : 이미지에서 객체의 위치와 크기를 탐지하기 위해 사용되는 사전 정의된 박스

## Introduction   
* 기존의 모델들은 속도와 정확도 간 trade-off를 통해 하나만을 살림
* Faster R-CNN보다 빠르고 YOLO보다 정확
* VGG-16 모델을 통해 인풋 이미지를 처리하여 저해상도에서도 높은 정확도를 보임
  > VGG-16 : Visual Geometry Group에서 개발한 이미지 인식 모델로 16 개의 계층으로 이루어짐
  
## The Single Shot Detector(SSD)

### Model
![image](https://github.com/sj990710/Thesis_Review/assets/127752372/70e17146-3356-480d-936a-ef4d812c268e)
* 사전 학습된 합성곱 신경망인 base network에 보조 네트워크,Extra Feature Layers(추가적인 합성곱 계층들)을 이어붙임

![image](https://github.com/sj990710/Thesis_Review/assets/127752372/29b14993-ea8e-4f9d-a47e-0dffa3c4b0b3)
* 실제로 detect 할 때는 NMS(Non-Max-Suppression)을 통해 줄어든 bounding box들을 이용
### Multi-Scale Feature Maps For Detection
* 7x7 사이즈의 feature map만을 사용했던 YOLO 1과 달리 다양한 사이즈의 feature map을 통해 다양한 크기의 객채 인
* 38x38, 19x19, 10x10, 5x5, 3x3, 1x1 6종류의 사이즈
* 작은 feature map에서는 큰 객체, 큰 feature map에서는 작은 개체 인식

### Convolutional Predictors For Detection
* 객체 p장의 3 x 3사이즈의 kernel이 있는 CNN으로 객체를 예측
* 일정한 사이즈의 예측값
* 예측한 bounding box의 값은 kernel이 convolution 연산을 적용한 영역 내 중심좌표와의 offset과 신뢰 점수를 나타냄

### Default Boxes And Aspect Ratios  
![image](https://github.com/sj990710/Thesis_Review/assets/127752372/96ddccba-063c-49e7-a15c-c46455c92c76)
![image](https://github.com/sj990710/Thesis_Review/assets/127752372/5d1a76ab-7790-4803-9fc7-22b963a01383)
  > s_k : 원본 이미지에 대한 k번째 feature map의 비율

  > m : feature map의 개수

![image](https://github.com/sj990710/Thesis_Review/assets/127752372/e4083d5b-3f6f-469d-95d4-802db664db31)

## Training(PASCAL VOC 데이터 셋. class 수: 20개)
![image](https://github.com/sj990710/Thesis_Review/assets/127752372/2dc5d624-0f5d-4119-a692-cfcddf382b31)

### Matching strategy
* ground truth와 default box를 미리 매칭 시켜 IOU가 0.5를 넘는 bounding box만 loss 계산에 사용
### Training objective 
![image](https://github.com/sj990710/Thesis_Review/assets/127752372/78bbf2b0-a7eb-4246-98ee-c92d2195c184)
![image](https://github.com/sj990710/Thesis_Review/assets/127752372/1b53adc0-bc60-4b3e-8f9a-30cbddf43ae2)
![image](https://github.com/sj990710/Thesis_Review/assets/127752372/a10b6685-1bdc-4bdb-a1e5-887e501b03cf)
* N : 매칭된 디폴트 박스 개수. N이 0이라면 L도 0이 됨
* 가중치 알파는 1로 설정
* Localization 손실: 디폴트 박스와 참 경계 박스 사이의 Smooth L1 손실
![image](https://github.com/sj990710/Thesis_Review/assets/127752372/f594b759-c926-4248-9bf6-a83a090d8756)

### Hard negative mining 
* 대부분의 default max는 negative임
* positive와 negative 사이에 불균형 발생
* confidence loss로 negative example 정렬 후 positive : negative = 1 : 3이 되도록 sample
### PASCAL VOC2007   
![image](https://github.com/sj990710/Thesis_Review/assets/127752372/aceef5f8-a983-4d3b-8a29-664942de4376)

### Model Analysis   
![image](https://github.com/sj990710/Thesis_Review/assets/127752372/c36531da-3169-47f1-b690-d9b96340fd47)

## Advantage and Disadvantage

### 장점  
* 다양한 feature map 사용해 다양한 크기의 물체들 인식 가능
* 6개의 bounding box를 통해 겹치는 좌표의 다양한 물체들도 인식 가능

### 단점  
* 여러 feature map의 detection을 계산하므로 compution cost 증가
