# Densely Connected Convolutional Networks(2017)

## Abstract
+ 최근의 CNN 연구들은 input 부근의 layer와 output 부근의 layer 사이의 connection이 짧을 수록 더 효과적인 training이 가능하다는 것을 증명하고 있음
  (Deep, Accurate, Efficient)

+ 이를 기반으로, 본 논문에서는 각 layer를 feed-forward 방식으로 다른 모든 layer들에 연결하는 고밀도 Convolution Network를 소개하려고 함
+ vanishing-gradient 개선, feature propagation 강화, feature reuse 권장, 학습 parameters 수 감소
+ 4개의 대표적인 데이터셋(cifar-10, cifar-100, SVHN, ImageNet)에서 모두 좋은 성능을 거두었으며, 계산량도 상대적으로 더 적었음


## Introduction
+ Lenet5의 5 layer ➝ VGG의 19 layer ➝ Highway Networks와 ResNets의 100+ layer
+ input이나 gradient에 대한 정보가 여러 layer를 계속 통과할수록 정보들이 점차 "씻겨 나간다"
+ 이 문제를 해결하기 위해, layer들을 연결한 model들이 등장하기 시작했다(ResNets, Highway Network, Stochastic depth, FractalNet)
 + 위 model들의 공통점은 **"선행 layer에서 후속 layer로 향하는 short path를 만든다는 것"**


![Figure 1](https://github.com/Artinto/2023-2_study/assets/84369594/0c139066-49f8-40b4-9a63-1114c3a5023b)

+ ResNets이 이전 output Feature map과 input Feature map의 summation으로 결과를 가져오는 것이었다면
  + $x_l = H_l(x_{l-1}) + x_{l-1}$

+ DenseNets은 이전 layer들로부터 생성된 모든 output Feature map들을 input layer와 합치는(concatenation) 방식
  + $x_l = H_l([x_0,x_1,...,x_{l-1}])$
  + 이러한 dense connectivity pattern으로 인해, 이 구조를 **DenseNet**이라 부른다.

-------------
   
+ Fewer Parameter
  + 불필요한 feature map들을 재학습할 필요가 없기 때문에 더 적은 Parameter를 가짐     
    (ResNet은 특성상 각 layer마다 weight가 서로 다르기 때문에 파라미터 수가 상당히 컸음)

+ Information preserved
  + DenseNet은 네트워크에 추가되는 정보와 보존되는 정보를 명확히 구분하여 정보를 보존함

+ Improve Flow of Information and Gradient
  + training에 용이하도록 정보와 gradient의 flow를 개선시켰으며, Overfitting을 방지하는 Regularization 효과까지 얻을 수 있음

## Related work


## DenseNets
![Figure 2](https://github.com/Artinto/2023-2_study/assets/84369594/ab4cff18-3b94-4d44-9a87-e75bbd607112)

![Table 1](https://github.com/Artinto/2023-2_study/assets/84369594/0934b2c8-a80d-4a3a-8406-387a3d66ad25)

## Experiments
![Tanle 2](https://github.com/Artinto/2023-2_study/assets/84369594/2880ad4e-f683-4ac2-9e73-4fd43ed7e4f6)
![Figure 3](https://github.com/Artinto/2023-2_study/assets/84369594/3f35be58-5dbb-457d-b891-9ba91e023d53)
![Figure 4)](https://github.com/Artinto/2023-2_study/assets/84369594/b753beba-75d5-4ea6-aa8d-42528399fbc7)
## Discussion
![Figure 4](https://github.com/Artinto/2023-2_study/assets/84369594/0c7eb6b8-fb40-4a54-a65e-b50134d7a96b)

![Figure 5](https://github.com/Artinto/2023-2_study/assets/84369594/61842b44-b2ce-4caa-b89c-1137376a302b)

