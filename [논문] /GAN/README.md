# GAN (2014)
**Generative Adversarial Nets**  
Review. KMJ, 2023.08.04

## Abstract
* adversarial process(적대적 프로세스)를 바탕으로 한 새로운 생성모델 프레임 워크
* generative model(생성 모델)과 discriminative model(식별 모델)을 경쟁적인 과정을 통해 동시에 학습
  > generator G: 입력 정보를 바탕으로 가상의 결과물을 만들어내는 모델
  
  > discriminator D: 생성데이터가 아닌 훈련 데이터에서 샘플이 나왔을 확률을 추정하는 모델
* GAN의 핵심은 다른 역할을 가진 두 모델을 통해 적대적 학습을 통해 '진짜같은 가짜'를 만들어내는 능력 기르기
* G는 훈련 데이터의 분포를 학습하여, 훈련데이터와 같은 분포로 생성
  > D가 데이터를 판별하는 확률이 1/2가 되도록 하는 것 (실제데이터와 G가 생성해 낸 데이터 구별 불가능)
* D는 실제 데이터와 G가 생성해낸 데이터를 구별
  > G가 만들어낸 Fake 이미지를 최대한 잘 판별하는 것
* z : 랜덤 벡터 (fake를 생성하기 위해 입력으로 넣는 노이즈)

![image](https://github.com/Artinto/2023-2_study/assets/108729047/0bc38be7-9a72-4c74-bc9b-c24071af945d)


## Introduction
- 이전의 딥러닝은 classification과 같은 분류 모델에서 크게 성공을 거둠 (discriminative model과 관련)
- 분류 모델은 gradient를 가지는 piecewise linear units(구간이 나뉘어진 선형 함수, ex.ReLU) 기반
- generative model은 비선형적이어야 하므로 piecewise linear units 사용 불가능
  - 다양하고 현실적인 데이터를 표현하기 위해서는 복잡한 비선형성 데이터를 포함해야함
  - Mode Collapse 문제 : 생성자가 모든 데이터의 다양성을 표현하지 못하고 특정 그룹(Mode)에서만 집중
  - Gradient Vanishing 문제 : 역전파 과정에서 그래디언트가 적절하게 전달되지 않아 모델 학습이 어려워짐 (학습 수렴 속도 느려짐)
- 다층 퍼셉트론과 경쟁 학습 방식을 통해 모델을 효과적으로 학습

![image](https://github.com/Artinto/2023-2_study/assets/108729047/12230ad8-858e-4382-ba9d-2039d809f39f)

- generator model은 random noise를 다층 퍼셉트론에 추가하여 모방 데이터 생성
- discriminative model은 다층 퍼셉트론에 데이터를 넣어 모방 데이터와 진짜 데이터를 구분
    > 다중 퍼셉트론을 사용하면 다른 복잡한 네트워크(CNN, Transformer)가 필요없이 순전파, 역전파, dropout만으로도 학습 가능
    
    > 역전파와 dropout을 통해 두 개의 모델 학습

    > 순전파를 통해 생성모델에서 모방 데이터 샘플링
    
## Related work

## Adversarial nets

### 다층 퍼셉트론
![image](https://github.com/Artinto/2023-2_study/assets/108729047/e55120b4-8fe9-4a54-a570-9445b2956bb9)  
퍼셉트론은 다수의 트레이닝 데이터를 이용하여 일종의 지도 학습을 수행하는 알고리즘

![image](https://github.com/Artinto/2023-2_study/assets/108729047/33a20f9d-f174-48a6-b706-23a238fe7cc9)  
중간층을 구성하는 노드가 여러개이고, 이러한 중간층이 다수로 구성되어 있는 구조


### 가치함수
* V는 학습 목표를 나타내는 가치함수
<img width="920" alt="obfunct_of_d" src="https://github.com/Artinto/2023-2_study/assets/108729047/d22d416e-4bb2-47bb-86e9-1af95afe263a">

* **D 목적** : 학습 데이터셋과 G에서 만든 데이터에 correct label을 할당할 확률을 **최대값으로 만드는** 것
* **G 목적** : D가 correct label을 제대로 할당할 수 없을 정도로 학습 데이터셋과 유사한 데이터를 만드는 것
  * log(1-D(G(z)))를 **최소값으로 만드는 것** (log 1 = 0) 
* log(D(x))는 D 최대, log(1-D(G(z)))는 G가 최소값으로 만드려는 대상
  
* log(D(x))가 0인경우 (


### 기본 구조
- 원본에 Z(random noise)가 포함된 G를 통해 가짜 데이터 생성
- G의 output을 D의 input에 넣어 classification
- 역전파 ( D의 loss 전달 및 G의 weight 업데이트 )
  - D는 loss만 확인할 뿐 업데이트 하지 않고 고정 ( weight freezing )
  - G는 weight를 업데이트 하여 D의 loss 줄이기
- 다시 업데이트 된 G로 가짜 데이터 생성
- D가 진짜와 가짜를 구분할 확률이 0.5가 될 때까지 반복

![image](https://github.com/Artinto/2023-2_study/assets/108729047/f826b06d-ef48-4521-88d2-15e76a1b4033)
> 검은 점선 : data generating distribution (실제 데이터 분포)  
> 파란 점선 : discriminator distribution (조건부 확률 분류 분포)  
> 녹색 점선 : generative distribution (가짜 데이터 분포)
> 하단 수평선의 화살표 위치가 0,1 판별 결과

* (a) 학습분포 초기 상태
* (b) 학습 초반에는 discriminator가 fake와 real을 잘 구분
* (c) generator 업데이트가 반복되면 점점 데이터의 분포가 비슷해져 판별하기 힘듦
* (d) 실제 데이터 분포와 G가 생성한 데이터 분포가 비슷해져서 1/2에 가까워짐

## Theoretical Results


## Experiments


## Advantages and disadvantages


## Conclusions and future work
