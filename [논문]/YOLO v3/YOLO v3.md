# YOLO v3(+v1 +v2)
**YOLO v3: an incremental improvement**   
Review.LSJ, 2023.08.25   
## Abstract 

> confidene(신뢰도 점수) : bbox가 객체를 포함하는지에 대해 신뢰성이 있는지, bbox가 얼마나 정확한지 반영

> Class probability  Pr(Class_i  |Object)  : 1. grid cell이 객체를 포함할 때 해당 개체가 i번째 클래스일 확률

> IoU : Intersection over Union

![image](https://github.com/sj990710/Thesis_Review/assets/127752372/4a0e4ffd-9d13-48f5-b4cd-d493294b0ac2)
# YOLO (You Only Look Once: unified real-time object detection)

## Introduction
* 기존의 2-stage 모델의 느린 속도를 보완하기 위해 만들어진 1-stage 모델

* object detection을 classification이 아닌 regression으로 접근

## Unified Detection (통합탐지)

* 이미지를 통째로 넣음으로써 global(상황이나 주제의 모든 부분을 포함)한 특성을 반영하며 detection
![image](https://github.com/sj990710/Thesis_Review/assets/127752372/6309213a-8b1d-4ed4-84b0-dd7febf337aa)
* Input image를 S x S 칸의 grid cell로 분할

* 각 grid cell들은 Bbox와 각 box들에 대한 confidence 및 class probability 예측
*  Confidence = Pr(Object) * IoU
*  각 grid cell 당 가장 큰 확률값을 갖는 하나의 클래스만 예측(YOLO는 20개의 class를 지원)
*  NMS(Non-maximal suppression)을 통해 detection 완료

## Network Design
*  24개의 convolutional layer(feature 추출)와 2개의 fully connected layer(예측)로 구성
*  중간중간 1 x 1 conolution layer를 사용 feature map의 demension 감소
*  output = 7 x 7 x 30 = (S x S x (5 * B + C))

## Training
*  주로 leaky ReLU 사용. 마지막 layer만 linear activation function 사용
*  SSE(Sum-squared Error)를 이용해 최적화
*  대부분의 grid cell은 confidence score가 0 -> 모델 불균형
*  λ_coord (= 5)와 λ_noobj (= 0.5)의 파라미터를 추가 -> bbox의 좌표 예측 손실 증가, 신뢰도 예측 손실 감소
*  Loss Function
 ![image](https://github.com/sj990710/Thesis_Review/assets/127752372/f353dec8-b17d-4c6d-a8e4-7d055b443693)

## Inference
*  이미지 한 장 98(7*7*2)개의 바운딩 박스 및 각 박스에 대한 클래스 확률 예측
*  하나의 객체를 여러 grid cell들이 detection 하는 경우 NMS을 통해 해결->mAP 2~3% 상승

## 한계점
*  새 떼와 같이 많은 수의 작은 객체들 detection 잘 못함
*  새로운 aspect ratio에 대한 탐지가 어려움
*  손실함수 SSE가 BB 크기와 관계 없이 가중치를 동일하게 취급한 문제를 해결하지 못함

# YOLO v2(9000: Better, Faster, Stronger)
*  Better : 정확도 증가
*  Faster : detection 속도 향상
*  Stronger : 더 많은 범위의 class 예측

## Better
* Batch Nomalization을 추가 -> mAP 2%가량 증가
* Convolutional with Anchor boxes -> mAP 0.3% 감소했지만 recall 4% 증가 => 개선될 여지가 있음
* Dimension Clusters 사용
>  일반적인  Euclidean distance 사용, 중심 좌표가 가장 짧은 것을 기준 시 IoU가 낮은 anchor 박스 선정 가능
>  IoU 기준으로 k-mean Clustering 사용
![image](https://github.com/sj990710/Thesis_Review/assets/127752372/faaf37f3-2458-4c48-8503-339418c077fd)
>  k : clustering의 개수. 논문에선 5개로 선정
![image](https://github.com/sj990710/Thesis_Review/assets/127752372/a6094704-b8f0-4217-8913-393b93405a1c)
* Direct location prediction
>  anchor box를 활용한 bbox offset 예측은 box의 위치를 제한 x -> 초기학습 시 불안정 -> 많은 시간 소요
>  sigmoid 함수 통해 offset 범위 0~1로 제한
![image](https://github.com/sj990710/Thesis_Review/assets/127752372/86226c14-8e00-4bfb-b634-f9b24eed20bb)
> 예측하는 범위가 정해짐으로써 안정적인 학습 가능

## Faster
* 대부분의 detection network는 VGG-16모델 사용 -> 뛰어나지만 너무 늦음
* Darknet-19 새로 디자인
  >  VGG-16 의 3 x 3 filter 사이에 1 x 1 filter로 차원 축소 및 FC layer 제거하여 연산량 감소

## Stronger
* classification data와 detection data를 학습에 같이 사용
* 전자 : classification 부분만, 후자는 loss function 전체를 이용해 backpropagation 진행
  >  class들이 exclusive 하지 않다
* Hierarchical classification를 가진 Word Tree 만듦
  ![image](https://github.com/sj990710/Thesis_Review/assets/127752372/d44df784-928d-4f8d-8db1-9d10c8c58b9d)

# YOLO v3( An Incremental Improvement)
## Bounding box prediction
* bbox의 objectness score도 예측
* bbox prior 와 ground truth의 IoU가 가장 크면 1, 아니며 전부 무시
## Class Prediction
* 각 bbox의 multilabel classification에 대한 결과 예측. Softmax < logistinc classfier
## Predictions Across Scales
* 마지막 layer의 feature만을 이용하지 않음
* 그 이전 layer의 feature map을 concatenation
* 이 과정을 통해 3개의 scale을 가진 feature map 이용
* N * N * [3 * (4 + 1 + 80)]
  >  3: bbox 개수, 4 : bbox의 offset (x,y,w,h), 1: objectiveness, 80: COCO 데이터 셋 class 개수
## 결과
* 320 x 320 입력에서 22ms속도 및 29.2mAP달성 -> SSD 수준의 정확도, 3배의 빠른 속도
* VOC 기준 RetinaNet 수준의 성능, 3.8배 빠른 속도
* COCO에서는 성능이 낮게 나옴. 객체에 정확하게 알맞는 bbox를 정하기 어려워 하는것으로 판단단
 
