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
    

## Adversarial nets

### 다층 퍼셉트론
![image](https://github.com/Artinto/2023-2_study/assets/108729047/e55120b4-8fe9-4a54-a570-9445b2956bb9)  
* 퍼셉트론은 다수의 트레이닝 데이터를 이용하여 일종의 지도 학습을 수행하는 알고리즘

![image](https://github.com/Artinto/2023-2_study/assets/108729047/33a20f9d-f174-48a6-b706-23a238fe7cc9)  
* 중간층을 구성하는 노드가 여러개이고, 이러한 중간층이 다수로 구성되어 있는 구조


### 가치함수
* V는 학습 목표를 나타내는 가치함수
<img width="920" alt="obfunct_of_d" src="https://github.com/Artinto/2023-2_study/assets/108729047/d22d416e-4bb2-47bb-86e9-1af95afe263a">

* G(Generator)를 minimize하고 D(Discriminator)를 maximize한다고 생각하면 된다.
* **D 목적** : 학습 데이터셋과 G에서 만든 데이터에 correct label을 할당할 확률을 **최대값으로 만드는** 것
* **G 목적** : D가 correct label을 제대로 할당할 수 없을 정도로 학습 데이터셋과 유사한 데이터를 만드는 것
  * log(1-D(G(z)))를 **최소값으로 만드는 것** (log 1 = 0) 
  
* 판별자가 모든 것을 분류 가능한 경우
  * D(x)=1, log(D(x))=0, D(G(z))=1, 
  * 수식의 앞 부분은 logD(x)는 0이 되어 사라지고, 뒷 부분은 log(1-1)이 되어 무한에 수렴
* 판별자가 모든 것을 분류하지 못하는 경우
  * G(z)=1, log(1-D(G(z))=0
  * 수식의 앞 부분인 logD(x)는 log0이 되어 무한에 수렴하게 되고, 뒷 부분인 log(1-D(G(z))는 0이 되어 사라지게 됨


### Architecture
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

## Experiments
- MNIST, TFD(Toronto Face Database), CIFAR-10에 대해 훈련
- 활성화 함수로 G는 ReLU와 시그모이드 함수 혼합, D는 maxout 함수 사용
- 이론적으로는 중간층에 dropout과 noise를 허용하지 않지만, 실험에서는 맨 하위 계층에 noise input 사용
- Parzen window 기반의 log 확률을 바탕으로 결과 측정 ( 확률을 다루기 힘든 모델을 평가할 때 사용 )
 <img width="395" alt="images_minkyu4506_post_401562be-e4e9-47c1-9420-5d1380bab1bb_스크린샷 2021-09-06 오전 1 32 53" src="https://github.com/Artinto/2023-2_study/assets/108729047/03752f8c-8414-419b-bfed-5ff043e36480">
- G가 생성해낸 sample이 기존 존재 방법으로 만든 sample보다 좋다고 주장 할 수는 없지만, 경쟁력이 있음
- 당시 저자의 지식으로 사용가능한 방식 중에서는 가장 좋은 평가 방식이지만, 고차원 데이터에서 평가하기 애매함

![img1 daumcdn](https://github.com/Artinto/2023-2_study/assets/108729047/d5e4c382-6efb-4fb5-83b1-db984d5a2ee3)
- 숫자와 얼굴의 경우 어느정도 식별이 가능하지만, 동물/사물에 대해서는 비교적 추상적으로 생성

## Advantages and disadvantages
### 장점
- 역전파로 그레디언트를 구할 수 있음
  - generator가 데이터셋에서 직접 업데이트 되지 않고 discriminator를 통한 gradient에서 업데이트
  - 입력의 구성요소가 generator 파라미터에 직접 복사되지 않음
- 학습 동안 추론이 필요 없음
- 다양한 함수들이 통합될 수 있음

### 단점
- p_g(x)의 명시적 표현이 없음
- G와 D가 동기화가 잘 되어야 함
  - G가 D의 학습 없이 혼자서 많이 학습되면 안됨
  - G만 계속 가중치를 조절하면, 노이즈를 같은 값으로 인식하면서 다양한 모델이 나오지 않음
