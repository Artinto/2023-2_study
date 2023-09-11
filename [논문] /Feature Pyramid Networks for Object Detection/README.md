# Feature Pyramid Networks for Object Detection

## Abstract
* Feature pyramids는 한 사물을 detection할 때 서로 다른 scale을 이용하여 분석하는 기법
* 사물에 대한 각각의 scale에 대해 접근 방식에 따라 해상도, 특성도, cost가 다름
* 본문은 Feature Pyramid Network(FPN)의 성능에 대해 이야기하고 있음

## Introduction

### Scale

<a href='https://ifh.cc/v-jGxz0K' target='_blank'><img src='https://ifh.cc/g/jGxz0K.jpg' width="600" height="300" title = "scale" border='0'></a>

### Feature Pyramid Architecture

<a href='https://ifh.cc/v-hpn4fS' target='_blank'><img src='https://ifh.cc/g/hpn4fS.png' border='0'></a>
> scale-invariant : scale이 변화여도 특징이나 객체법칙에 대해 무관
> > 위 Pyramids는 사전에 scale작업 후 연산에 들어가기 때문에 scale-invariant함

#### Convolutional neural network(CNN)

<a href='https://ifh.cc/v-THQSsZ' target='_blank'><img src='https://ifh.cc/g/THQSsZ.jpg' border='0'></a>

#### Sementic gap

<a href='https://ifh.cc/v-PHOXRM' target='_blank'><img src='https://ifh.cc/g/PHOXRM.png' width="350" height="200" border='0'></a> <a href='https://ifh.cc/v-J8zh2p' target='_blank'><img src='https://ifh.cc/g/J8zh2p.jpg' width="350" height="200" border='0'></a>

* 위와 같은 feature pyramid구조상 scale이 클 수록 낮은 특성의 feature이고 scale이 작을 수록 높은 특성의 feature라고 할 수 있음
* 또한 특성도에 따라 다양한 패턴이 보여지게 되는데 low-level feature와 high-level feature의 차이가 커지게 되고 이를 Sementic gap이라 하며 이 sementic gap은 인식률을 낮춤
* 이를 보안하기 위해 FPN이 고안


## Feature Pyramid Networks(FPN)

### Architecture
<a href='https://ifh.cc/v-avlHpZ' target='_blank'><img src='https://ifh.cc/g/avlHpZ.jpg' border='0'></a>

### Bottom-up pathway & Top-down pathway

<a href='https://ifh.cc/v-tm1Ghb' target='_blank'><img src='https://ifh.cc/g/tm1Ghb.jpg' width="350" height="500" border='0'></a> <a href='https://ifh.cc/v-VgkGnx' target='_blank'><img src='https://ifh.cc/g/VgkGnx.png' width="350" height="200" border='0'></a>

#### Bottom-up pathway
* 이미지를 convolutional network에 입력하여 forward pass하여 2배씩 작아지는 feature map을 추출하는 과정

#### Top-down pathway
* 각 stage에서 추출된 feature map을 2배로 upsampling하는데 이때 nearest neighbor upsampling방식을 이용
> neighbor upsampling : scale을 키우는데, 키운 위치에서 원본에서 가장 가까운 값을 그대로 적용하는 방법


#### Lateral connection architecture
<a href='https://ifh.cc/v-qNGpZL' target='_blank'><img src='https://ifh.cc/g/qNGpZL.jpg' border='0'></a>

#### Faster-RCNN with FPN
<a href='https://ifh.cc/v-9aPh1J' target='_blank'><img src='https://ifh.cc/g/9aPh1J.jpg' border='0'></a>


<a href='https://ifh.cc/v-rHwCdy' target='_blank'><img src='https://ifh.cc/g/rHwCdy.jpg' border='0'></a>

## Experiments

<a href='https://ifh.cc/v-7GkhAm' target='_blank'><img src='https://ifh.cc/g/7GkhAm.png' border='0'></a>

<a href='https://ifh.cc/v-Y1foNb' target='_blank'><img src='https://ifh.cc/g/Y1foNb.png' border='0'></a>

<a href='https://ifh.cc/v-1cYVjF' target='_blank'><img src='https://ifh.cc/g/1cYVjF.png' border='0'></a>



