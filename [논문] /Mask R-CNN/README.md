# Mask R-CNN

## Abstract
* 기존 Faster R-CNN에서 BBox recogition branch에서 Mask branch를 추가
* 훈련이 간단해지며 5fps로 조금의 Overhead가 발생
* Including instance segmentation, Bounding box object detection, Person keypoint detection 등의 COCO 과제 세트에서 우수한 결과를 보임

## Introduction

### Segmentation

* 기존 Object detection과는 다르게 pixel 수준에서 각 영역이 어떤 의미(특징)을 갖는지 분리하는 method

<img src="https://ifh.cc/g/g5VOZY.jpg" width="500" height="250"/>

  * Semantic Segmentation Vs Instance Segmentation    
    <img src="https://ifh.cc/g/Ha04p9.png" width="500" height="250"/>
    > Instance Segmentaion은 Semantic Segmentation과 달리 class만 구분하는 것이 아닌 instance까지 구별함

### Faster R-CNN

<a href='https://ifh.cc/v-9aPh1J' target='_blank'><img src='https://ifh.cc/g/9aPh1J.jpg' border='0'></a>

## Mask R-CNN

* 기존 Sementic Segmentation에서 instance를 구분하지 못한다는 한계점을 Object Detection method와 결합시켜 pixel단위로 instance도 구분할 수 있는 task로 제안됨

<img src="https://ifh.cc/g/6Jr2sm.png" width="500" height="250"/>

> 본문에서는 Object Detection method로 Faster R-CNN을 채택

>> RoI Algin에서 도출된 Feature map을 가져와 Classifer와 Bounding box regressor와 평행한 Mask branch로 진행

### Head Architecture

<img src="https://ifh.cc/g/XQtHvK.jpg" width="300" height="180"/><img src="https://ifh.cc/g/tpfmOS.jpg" width="400" height="180"/>

> Mask branch내부안에서는 cnv layer가 존재하는데 위 그림의 경우 각각 ResNet C4와 FPN 백본용 헤드 기준의 구조를 보여줌

### RoI Algin

<img src="https://ifh.cc/g/RcGLBa.jpg" width="400" height="180"/>

> RoI pooling

* RoI pooling은 RoI의 소수점 좌표를 반올림하여 pooling하기 때문에 위치정보가 왜곡되는 Misaligment가 발생하여 pixel Mask를 예측하는데 장애요소가 됨

<img src="https://ifh.cc/g/3qyKoo.png" width="800" height="90"/>
<img src="https://ifh.cc/g/zN2hdf.jpg" width="800" height="200"/>
<img src="https://ifh.cc/g/Z55ZVQ.png" width="400" height="180"/>
<img src="https://ifh.cc/g/fVJ98W.jpg" width="800" height="200"/>

### Loss Function

$$
L = L_{cls} + L_{box} + L_{mask}
$$

$L_{cls}$ : Softmax cross entropy

$L_{box}$ : Regression

$L_{mask}$ : Binary cross entropy

## Experiments

### Instance segmentation

<img src="https://ifh.cc/g/HQDQaf.png" width="800" height="200"/>

### Object detection

<img src="https://ifh.cc/g/1LbaVz.jpg" width="800" height="200"/>

<img src="https://ifh.cc/g/x5vSPO.png" width="800" height="200"/>

<img src="https://ifh.cc/g/jAFrqA.png" width="800" height="200"/>

### Person keypoint detection

<img src="https://ifh.cc/g/XS0KFC.jpg" width="800" height="200"/>

<img src="https://ifh.cc/g/bFYGbA.jpg" width="800" height="200"/>
