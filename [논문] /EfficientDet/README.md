# EfficientDet: Scalable and Efficient Object Detection(2019)

## Abstrac
* Computer Vision 분야에서 model의 efficiency의 증가가 중요하게 여겨지고 있는데 본문에서는 efficiency를 증가시키는 새로운 object detection과 그에 따른 몇가지 optimization을 제안하고 있음
* 그중 기존의 FPN의 구조를 변형시킨 bi-directional feature pyramid network(BiFPN)을 제안
* 해상도, 깊이, 너비 등 다차원에 대한 scailing method를 제안

## Introdution
* 당시 로보틱스나 자율주행 같은 경우 object detection 모델이 매우 크고 cost가 매우 커 현실적으로 적용하기 힘듦
* 당시 대부의 모델들은 높은 정확도와 효율성을 위해 특정적이고 작은 범위의 resource를 이용했기에 현실적으로 적용시키기 위해선 다양하고 많은 resource에 대응해야 하는 어려움이 있음
* 본문에서는 높은 정확도와 더 나은 효율성을 가지는 다양한 resource 제약에 확장이 가능한 탐지 구조를 제안
* Efficient multi-scale feature fusion(기존에는 단순히 더했는데 이는 각 feature마다 output feature에 기여도가 다름)
* Model scaling(한 차원만 scaling하는 것이 아닌 모든 차원의 scailing을 해줘야함)
* 위 두 문제점을 해결하기 위해 combining EfficientNet backbones with BiFPN and Compound Scaling을 진행

<img src="https://ifh.cc/g/XSJ1Qf.png" width="500" height="450"/>

### BiFPN

#### BiFPN - Problem Formulation

$$
\overrightarrow{P^{in}} = (P^{in}_{l1} , P^{in}_{l2}, ...)
$$


$$
\overrightarrow{P^{out}} = f(\overrightarrow{P^{in}})
$$

<img src="https://ifh.cc/g/s89pHv.jpg" width="1000" height="350"/>

##### FPN

<img src="https://ifh.cc/g/qpZBoh.png" width="300" height="200"/>

* one-way information flow의 한계가 존재

##### PANet

* 앞의 top-down path의 FPN형식에 bottom-up path를 더함

##### NAS-FPN

* Neural Architecture Search(NAS)를 이용한 FPN
* irregular하고 해석과 수정이 어려움

#### BiFPN - Cross-Scale Connections

* 본문에 따르면 PAnet이 FPN과 NAS-FPN보다 더 좋은 accuracy을 보였다 함
* 그러나 parameter와 computation의 cost문제가 발생

<img src="https://ifh.cc/g/fcAbSD.png" width="300" height="400"/>

1) 1개의 input edge만 있는 node제거
2) input에서 output node로의 edge추가
3) Repeated block으로 high-level feature fusion 진행

#### BiFPN - Weighted Feature Fusion

* Weighted fusion approaches : input feature의 중요도를 학습하는 weigh를 추가
* Fast normalized fusion : 기존의 softmax가 아닌 activation function

<img src="https://ifh.cc/g/gMMmqn.jpg" width="350" height="200"/><img src="https://ifh.cc/g/HwDKtn.jpg" width="350" height="400"/>

#### BiFPN - EfficientDet Architecture

* Backbone : EfficientNet
<img src="https://ifh.cc/g/KWdjod.png" width="1000" height="400"/>

* Focal Loss 사용 : classified하기 쉬운 예제들에 대해서 loss를 적게 줌
<img src="https://ifh.cc/g/40xdfh.png" width="300" height="200"/>

### Compound Scaling

* EfficientNet에서 제안된 Compound Scaling을 사용, backbone network, BiFPN network, class/box network, resolution을 전부 scale up

<img src="https://ifh.cc/g/25zDwH.jpg" width="300" height="200"/>
>  d,w,r 이 3개를 조합하는 것만으로도 효율적이고 좋은 성능을 기대할 수 있음

* 다만 너무 많은 dimension으로 인해 Heuristic-based scaling으로 개발

<img src="https://ifh.cc/g/X8644y.jpg" width="1000" height="400"/>

### Experiments

<img src="https://ifh.cc/g/L89ORV.jpg" width="1000" height="500"/>

<img src="https://ifh.cc/g/QSfQaP.jpg" width="1000" height="300"/>

### Ablation Study

#### Disntangling backbone and BiFPN

<img src="https://ifh.cc/g/CzbaMJ.png" width="400" height="250"/>

#### Comparsion of different feature networks

<img src="https://ifh.cc/g/FzYL0Y.png" width="400" height="250"/>

#### Comarsion of different feature fusion

<img src="https://ifh.cc/g/CRgFk1.png" width="400" height="250"/>


 
