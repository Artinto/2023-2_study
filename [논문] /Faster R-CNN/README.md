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
  
* 각 anchor에 대해 binary class label을 진행하는데 있어 positive label을 찾아내는데 두가지 방식의 ankhor가 존재
  * Intersection-over-Union(IoU)
      ![IoU](https://blog.kakaocdn.net/dn/I9MIb/btq9eMfNYbF/KeQxOsQydbNkZuRNhoMv9k/img.png "IoU")
    * 위 그림처럼 box들이 얼마나 겹쳐 있는지에 따라 positive label(>=0.7/유), neagtive label(<=0.3/무)을 구분





  










## 5 Experiments


## 6 Conclusion






