# Faster R-CNN: Towards Treal-Time Object Detection with Region Proposal Networks(2015)

## Abstract
* 당시 2015년, SPPnet과 Fast R-CNN과 같은 Object detection은 detection의 시간은 감소했지만 Region Proposal단계에서 시간 소요를 보안 하기 위해 Faster R-CNN이 제안
* Faster R-CNN은 기존 Fast R-CNN의 물체의 위치를 알아내는 Region Rroposal을 별도의 Region Rroposal Networks(RPN)를 추가하여 GPU를 사용하여 시간 단축
* Detection Network와 RPN은 같은 convolutional features를 공유하기에 region proposal cost는 없음
* Fast R-CNN은 Region Proposal을 cpu기반으로 했지만 Faster R-CNN 경우 별도의 RPN을 추가하여 GPU를 사용함으로써 속도 측면에서 큰 개선이 이뤄짐

## 1 Introduction
* Faster R-CNN 이전의 object detection은 cpu에서 bottleneck이 발생하기 때문에 region proposal에 시간이 오래 걸림
* Region proposal 단계에서 Selective Search가 각 이미지에 대해 2초정도의 시간이 소요됨으로 굉장히 느림
* 그래서 Region proposal을 GPU로 올리면서 개선 가능, 다만 Region proposal을 담당하는 Network를 두는 경우 sharing computation 가능에 의문
* 본 논문에서는 알고리즘 측면에서 변화를 이용하여 region proposal computation을 cost-free하도록 Network를 구성
* Detection network와 feature map들을 공유하여 성능도 좋아지고 시간적인 측면에서도 이점을 보임
* Feature map 자체가 앞쪽에서 sharing 된다면 별도의 RPN을 구축하는데 있어서 추가적인 몇개의 convolution layer만 있어도 가능하기에 cost-free
* 본 논문에서는 Faster R-CNN에서 기존의 region proposal을 위한 selective search에서 시간을 사실상 없는 것으로 하여 시간적 측면에서 이점이 있음
* MS COCO, PASCAL VOC와 같은 데이터셋에서 우수한 성능을 보임

## 2 Related Work
### Object Proposal Method
  * Selective Search
    * object 인식이나 검출을 위한 가능한 후보 영역을 알아낼 수 있는 방법을 제공하는 것을 목표(기존 Fast R-CNN은 CPU기반)
  * Sliding Window
    * 일정 크기의 Window를 이미지 위에서 조금씩 옮기면서 '전수조사'하는 것(한 이미지에 대해 윈도우를 sliding하는 것으로 비효율적)
### Deep Networks for Object Detection
  * 초창기 R-CNN은 물체가 어디 있는지는 GPU를 사용하지 않음, CPU를 이용한 Selective Search 사용(Region Proposal에 대해 bounding이 심함)
  * 그래서 Deep Networks를 이용하여 bounding box를 찾아내는 방법들이 제안되었음(Ex. OverFeat, MultiBox)

## 3 Faster R-CNN

![Figure 1: Faster R-CNN is a single, unified network for object detection](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FRWpKA%2FbtqQCApKJ3R%2FxU6cjtRW6RDksmje7X4RzK%2Fimg.png "Figure 1: Faster R-CNN is a single, unified network for object detection")

* Image를 Conv layers를 통과하여 feature map이 형성되는데 이 feature map은 RPN과 RoI pooling에 공유되고 RPN의 결과를 다시 RoI pooling에 사용되어 classifier를 진행
* 이처럼 Faster R-CNN은 두가지 모듈로 구성되어 있는데 기존 fast R-CNN의 Detector와 RPN으로 구성

## 4 Region Proposal Networks

![Figure 2: Region Proposal Network(RPN)](https://ifh.cc/g/PfKnzG.jpg "Figure 2: Region Proposal Network(RPN)")

* RPN은 input으로 한장의 이미지를 받아 bounding box의 형태로 output을 출력
* 이때 사용되는 feature map은 Fast R-CNN과 공유하여 사용
* RPN을 진행하는데 있어 n x n 크기의 window를 feature map에 sliding하여 진행(이때 feature는 각각 reg, cls용으로 두개로 진행)
### Faster R-CNN RPN의 특성

#### Anchor
  
* 이러한 sliding-window location에 대하여 다양한 Region Proposal을 예측하는데 본문에서는 Anchor라고 표현
* 위치마다 k개의 box를 이용(다양한 size)
* cls layer의 경우 object의 유무를 판단하기 위해 softmax형태의 2k score가 나타남
* reg layer의 경우 object의 위치를 판단하기 위해 가로,세로,높이,너비에 대해 4k로 예측(본 논문에서는 기본적으로 3 scale, 3 aspect ratios를 이용하기에 총 k=9의 ankhor를 사용)
* Feature map의 size가 W x H라고 한다면 ankhor의 갯수는 WHk개가 됨

#### Translation-Invariant Anchors
  
* 이미지에서 이동이 가해진다 하더라도 Translation-Invariant가 보장
* Multibox와 같이 Translation-Invariant가 보장되지 않는다면 Overfitting의 위험도가 큼
    
#### A Loss Function for Learning Region Proposals
  
* Intersection-over-Union(IoU)

 ![IoU](https://blog.kakaocdn.net/dn/I9MIb/btq9eMfNYbF/KeQxOsQydbNkZuRNhoMv9k/img.png "IoU")
  * IoU가 가장 높은 것은 positive label로 취급
  * 또는 IoU값이 각각 positive label(>=0.7/유), neagtive label(<=0.3/무)로 취급

* Loss Function
  * IoU를 통해 positive도 negative도 아닌 것은 object function에 영향을 미치지 않기에 아래와 같은 loss function을 이용
<a href='https://ifh.cc/v-wnSyKq' target='_blank'><img src='https://ifh.cc/g/wnSyKq.png' border='0'></a>

  * cls에서 pi*의 경우 ground-trurh(정답 lable)은 ankhor에 따라 1 or 0의 값을 가지고 reg은 현재 위치에 object가 존재할때만 정확한 위치를 찾아내는 네트워크이기에 cls에서 1일 경우만 진행, 0일 경우 생략(ti*는 물체의 가로,세로,너비,높이를 가지고 있는 튜플)
  * sigma앞에 있는 것은 weight함수로 각 loss에 대한 가중치로 ankhor개수로 정해짐(크게 영향을 미치진 않음)
<a href='https://ifh.cc/v-Dv9cD1' target='_blank'><img src='https://ifh.cc/g/Dv9cD1.png' border='0'></a>
  * bounding box regression을 위한 파라미터 공식들은 위와 같이 기본 R-CNN의 parameterization을 이용(x,y는 box의 center)

  #### Sharing Convolutional Features for Region Proposal and Object Detection

  1. 위 설명처럼 RPN을 훈련 후 end-to-end로 fine-tuning
  2. detection network를 ImageNet에 의해 초기화 후 Fast R-CNN으로 훈련, 이때 RPN과 detection network는 conv layer를 공유하지 앟음
  3. 네트워크 간 conv layer를 공유하기 위해 수정한 뒤 RPN의 하이퍼파라미터를 fine-tuning 후 두 네트워크에 합성곱 layer를 공유
  4. 공유 conv layer를 고정하여 Fast R-CNN의 fc layer를 fine-tuning

## 5 Experiments

### PASCAL VOC 2007 test set(+Ablation Experiments)

<a href='https://ifh.cc/v-Brqs66' target='_blank'><img src='https://ifh.cc/g/Brqs66.png' border='0'></a>
> 이 논문에서 제안한 Fast R-CNN에 RPN을 추가하여 서로 conv layer를 sharing할 때 성능이 좋음
> conv layer를 sharing할때 성능이 더 좋음
> ZF보다 VGG를 사용했을 때 더 성능

### Perfomance of VGG-16

<a href='https://ifh.cc/v-CHB7GP' target='_blank'><img src='https://ifh.cc/g/CHB7GP.png' border='0'></a>
> 같은 data set을 이용할 때 확실히 selective search보다 RPN+VGG를 이용한 것이 성능이 우수하며 시간도 단축 됨

### Timing

<a href='https://ifh.cc/v-FjLGop' target='_blank'><img src='https://ifh.cc/g/FjLGop.png' border='0'></a>
> ss와 RPN을 비교하였을 때 proposal의 수가 감소하여 속도가 증가함
> ZF보다 VGG가 더 deep network이기에 VGG 속도가 비교적 느림

### Analysis of Recall-to-IoU

<a href='https://ifh.cc/v-4j21rn' target='_blank'><img src='https://ifh.cc/g/4j21rn.png' border='0'></a>
> IoU측면에서 RPN을 사용했을 때 다른 method에 비해 성능이 우수함을 알 수 있음

### One-Stage Detection vs Two-stage Detection(Proposal + Detection)

<a href='https://ifh.cc/v-S5q0qn' target='_blank'><img src='https://ifh.cc/g/S5q0qn.png' border='0'></a>

## 6 Conclusion

* conv layer를 RPN과 detection network에 공유함으로써 cost-free상태로 객체 감지 정확도를 향상시키고 시간을 단축하는데 있어 우수함






