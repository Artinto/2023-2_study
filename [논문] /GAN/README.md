# GAN (2014)
**Generative Adversarial Nets**  
Review. KMJ, 2023.08.04

## Abstract
* adversarial process(적대적 프로세스)를 바탕으로 한 새로운 생성모델 프레임 워크
* generative model(생성 모델)과 discriminative model(식별 모델)을 경쟁적인 과정을 통해 동시에 학습
  > generator G: 입력 정보를 바탕으로 가상의 결과물을 만들어내는 모델
  
  > discriminator D: 생성데이터가 아닌 훈련 데이터에서 샘플이 나왔을 확률을 추정하는 모델
* G는 훈련 데이터의 분포를 학습하여, 훈련데이터와 같은 분포로 생성
  > D가 데이터를 판별하는 확률이 1/2가 되도록 하는 것 (실제데이터와 G가 생성해 낸 데이터 구별 불가능)
* D는 실제 데이터와 G가 생성해낸 데이터를 구별
  > G가 만들어낸 Fake 이미지를 최대한 잘 판별하는 것

![image](https://github.com/Artinto/2023-2_study/assets/108729047/0bc38be7-9a72-4c74-bc9b-c24071af945d)


## Introduction
- 이전의 딥러닝은 classification과 같은 분류 모델에서 크게 성공을 거둠 (discriminative model과 관련)
- 분류 모델은 backpropagation(역전파)와 dropout 알고리즘에 기반
- gradient를 가지는 piecewise linear units(구간이 나뉘어진 선형 함수, ex.ReLU) 사용하여 generative model에 적용하기 어려움
- 제어하기 힘든 probabilistic computations(최대 확률 추정 등의 분야에서 사용)을 추론하기 어려움  
![image](https://github.com/Artinto/2023-2_study/assets/108729047/12b20019-7758-4b41-98df-cf4f67ee67da)  

- generator model은 random noise를 다중 퍼셉트론에 추가하여 모방 데이터 생성
- discriminative model은 다중 퍼셉트론에 데이터를 넣어 모방 데이터와 진짜 데이터를 구분
    > 다중 퍼셉트론을 사용하면 다른 복잡한 네트워크가 필요없이 순전파, 역전파, dropout만으로도 학습 가능
    
    > 역전파와 dropout을 통해 두 개의 모델 학습

    > 순전파를 통해 생성모델에서 모방 데이터 샘플링
    
## Related work


## Adversarial nets


## Theoretical Results


## Experiments


## Advantages and disadvantages


## Conclusions and future work
