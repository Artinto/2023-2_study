# Faster R-CNN: Towards Treal-Time Object Detection with Region Proposal Networks

## Abstract
* 당시 2015년, SPPnet과 Fast R-CNN과 같은 Object detection은 detection의 시간은 감소했지만 Region Proposal단계에서 시간 소요를 보안 하기 위해 Faster R-CNN이 제안
* Faster R-CNN은 기존 Fast R-CNN의 물체의 위치를 알아내는 Region Rroposal을 별도의 Region Rroposal Networks(RPN)를 추가하여 GPU를 사용하여 시간 단축
* Detection Network와 RPN은 같은 convolutional features를 공유하기에 region proposal cost는 없음
* RPN은 end-to-end 방식으로 학습이 가능
* Fast R-CNN은 Region Proposal을 cpu기반으로 했지만 Faster R-CNN 경우 별도의 RPN을 추가하여 GPU를 사용함으로써 속도 측면에서 큰 개선이 이뤄짐

## 1 Introduction
* Faster R-CNN 이전의 object detection은 cpu에서 bottleneck이 발생하기 때문에 region proposal에 시간이 오래 걸림
* Region proposal 단계에서 Selective Search가 각 이미지에 대해 2초정도의 시간이 소요됨으로 굉장히 느림
* 그래서 Region proposal을 GPU로 올리면서 개선 가능, 다만 Region proposal을 담당하는 Network를 두는 경우 sharing computation 가능에 의문
* 본 논문에서는 알고리즘 측면에서 변화를 이용하여 region proposal computation을 cost-free하도록 Network를 구성
* Detection network와 feature map들을 공유하여 성능도 좋아지고 시간적인 측면에서도 이점을 보임
* Feature map 자체가 앞쪽에서 sharing 된다면 별도의 RPN을 구축하는데 있어서 추가적인 몇개의 convolution layer만 있어도 가능하기에 cost-free

## 2 Related Work
* 

## 3 Region Proposal Networks


## 4 Experiments


## 5 Conclusion






