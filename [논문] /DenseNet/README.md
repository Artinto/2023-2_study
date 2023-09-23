# Densely Connected Convolutional Networks

## Abstract
+ 최근의 CNN 연구들은 input 부근의 layer와 output 부근의 layer 사이의 connection이 짧을 수록 더 효과적인 training이 가능하다는 것을 증명하고 있음
+ 이를 기반으로, 본 논문에서는 각 layer를 feed-forward 방식으로 다른 모든 layer들에 연결하는 고밀도 Convolution Network를 소개하려고 함
+ 지금부터 소개할 DenseNet은 vanishing gradient 개선, feature propagation 강화, feature reuse 권장, 학습 parameters 수 감소 등의 장점을 갖고 있음
+ 4개의 대표적인 데이터셋(cifar-10, cifar-100, SVHN, ImageNet)에서 모두 좋은 성능을 거두었으며, 계산량도 상대적으로 더 적었음


## Introduction
+ Lenet5의 5-layer -> Highway Networks와 ResNets의 over 100-layer
+ input이 layer를 계속 통과할수록 정보들이 점차 "씻겨 나간다"
+ 이 문제를 해결하기 위해, layer들을 연결한 model들이 등장하기 시작했다(ResNets)
  
+ ResNets이 이전 output Feature map과 input Feature map의 summation으로 결과를 가져오는 것이었다면
  + $x_l = H_l(x_{l-1}) + x_{l-1}$

+ DenseNets은 이전 layer들로부터 생성된 모든 output Feature map들을 input layer와 Concatenation하는 방식
  + $x_l = H_l([x_0,x_1,...,x_{l-1}])$


![Figure 1](https://github.com/Artinto/2023-2_study/assets/84369594/0c139066-49f8-40b4-9a63-1114c3a5023b)

+ Fewer Parameter

+ Information preserved

+ Improve Flow of Information and Gradient

## Related work

## DenseNets

## Experiments

## Discussion
