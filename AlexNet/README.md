# ImageNet Classification with Deep Convolutional Neural Networks

## Abstract
* large, deep convolutional neural network
* top-1 and top-5 error는 각각 37.5%, 17.0%
* 5개의 convolution layers, 일부는 max-pooling layer와 3개의 fully connected layer, softmax
* fully connected layer의 overfitting을 줄이기 위해 dropout 사용

## Introduction
* CNN 모델은 깊이과 너비를 다양하게 조절 가능하고 이미지에 대해 대부분 정확한 예측을 함
* 다른 비슷한 신경망에 비해 더 적은 연결과 파라미터로 훈련이 가능하고 이론상 더 좋은 효과를 가짐
* 하지만 고해상도의 큰 데이터 셋에 적용하기에는 여전히 힘들었음
* AlexNet은 성능을 올리고 훈련시간을 줄일 수 있는 새로운 특징을 발견하였다.
* 5개의 convolution layer + 3개의 fully-connected layer를 사용했으며, GTX580 3GB GPU 2개를 이용하여 훈련을 진행헀으며 좋은 성능을 보였다.


## The Dataset
* IamgeNet : 22000개의 카테고리에 속하는 15 million 이상의 이미지
  > ILSVRC(ImageNet Large-Scale Visual Recognition Challeng)에서 사용하는 데이터셋
  
  > 1000개의 카테고리에 대해 약 1000장의 이미지를 제공
* IamgeNet에서 제공하는 이미지는 가변적이지만, AlexNet은 일정한 입력 차원이 필요
* 256x256으로 이미지 조정
* 직사각형이미지가 주어지면 짧은 면의 길이가 256이 되도록 resize 후 256x256 사이즈에 맞게 중앙에서 잘라내는 방식


## The Architecture
5개의 convolution layer + 3개의 fully-connected layer


### ReLU Nonlinearity
* 기존에는 Activation Function으로 tanh와 sigmoid 주로 사용, AlexNet에서는 ReLU 사용
  > 깊은 네트워크 구조때문에 빠르게 학습할 수 있는 능력이 요구되므로 채택
* ReLU는 x값이 양수일 결우 기울기가 일정하므로 gradient vanishing 현상 X, 연산 비용이 비교적 적다.

<p align="center"><img width="432" alt="스크린샷 2022-10-12 오후 11 56 33" src="https://user-images.githubusercontent.com/56713634/195377436-cf748936-0d62-4eb3-91d1-79e919d1fedb.png"></p>
* CIFAR-10을 가지고 비교한 결과 25% training error rate에 도달하는 시간이 6배 가량 빠르다고 한다.


### Training on Multiple GPUs
* 1.2 milion training data를 사용하기에 1개의 GPU로 불가능, 두 개를 병행하여 사용
* GPU는 병렬화에 잘 작동하고 주메모리에 접근할 필요없이 서로의 메모리에서 읽고 쓰기 가능 

#### cross-GPU parallelization
* kernel을 반으로 나눠 각각의 GPU가 담당하게 하는 방식
* 특정 layer에서만 GPU가 서로 상호 작용
  > 3번째 convolutional layer와 FC(Fully connected) layer를 제외하면 독립적으로 훈련
* GPU를 하나만 썼을 경우와 비교하여, training error를 1~2% 가량 줄였고 시간도 약간 더 빠름


### Local Response Normalization
* ReLU를 사용하면 normalization이 필수가 아님
* 하지만 큰 양수 값이 들어오면 값이 더욱 커지게 되어 다른 값에 영향을 미칠수도 있음
* AlexNet에서는 local response normalization를 적용해 오차를 약 1~2% 줄임

<p align="center"><img width="417" alt="스크린샷 2022-10-12 오후 10 54 39" src="https://user-images.githubusercontent.com/56713634/195377707-1b039741-43a8-41d6-9ca6-f4cc8d685499.png"></p>

> a^i_x, y : (x,y)에 위치한 픽셀(뉴런)에 i번째 kernel을 적용하고 ReLU를 사용했을 때 나온 activation value.

> n : 인접하다고 고려할 뉴런의 개수(하이퍼파라미터). n에 따라 j의 범위가 늘어나고 줄어든다.

> N : 레이어 안에 존재하는 kernel 총 개수


* kernel에 비해 큰 값이 나온 곳을 정규화하는 방법
* i번째 kernel map의 x,y 지점의 값을 (i-n/2)번째~(i+n/2)번째 kernel map의 x, y 지점의 값들을 더해 나눈다.
* k = 2, n = 5, α = 10−4, β = 0.75 는 여러 연구를 통해 알아낸 최적의 수치이며 이는 하이퍼 파라미터이다. 


### Overlapping Pooling
* CNN에서 일반적으로 Pooling은 필터가 겹치지않고 적용된다
  > stride = pool_size
* Alexnet에서는 필터가 겹치도록 설계
  > stride=2, pool_size=3 
*  top-1 error rate와 top-5 error rate가 각각 0.4%, 0.3% 줄임

### Overall Architecture
<p align="center"><img width="964" alt="스크린샷 2022-10-12 오후 11 10 00" src="https://user-images.githubusercontent.com/56713634/195378313-580e5546-9ebd-4625-95eb-819651916c22.png"><p>

* 8개의 layer
* 5개가 Convolutional Layer, 3개가 FC Layer, FC Layer의 마지막 부분은 softmax함수를 사용하여 1000개의 output
* 2, 4, 5번째 Convolutional Layer는 이전 레이어에서 같은 GPU에 존재하는 Kernel map에서만 input을 
* 3 번째 Convolutional Layer에서는 모든 kernel map들로부터 input을 받아들인다.
* FC Layer의 각 뉴런들은 이전 레이어의 모든 뉴런들과 연결
* Response-Normlization layer(LRN)이 첫 번째와 두 번째 Layer 다음에 연결
* max-pooling은 LRN 뒤에랑 다섯번째 convolution layer에서 사용하였다.
* ReLU non-linearity는 모든 convolution layer와 fully-connected layer에서 사용되었다.

## Reducing Overfitting

### Data Augmentaion
label-preserving transformation(라벨 보존 변형)을 사용하여 데이터셋을 늘림

#### image translations 과 horizontal reflections
* 256 X 256 크기의 이미지에서 랜덤하게 224 X 224 크기의 데이터를 추출
* horizontal reflections하여 만들면 데이터셋이 2048배로 늘어난다. 
> 이러한 증감 기법을 사용하지 않으면 overfit으로 인하여 깊은 네트워크 사용 불가능
* test시  224 x 224 patch들을 총 5개(좌상단, 우상단, 우하단, 좌하단 꼭지점에 붙인 4개의 patch와 가운데 patch 1개)와 이를 horiozntal flip하여 총 10개의 patch 뽑아냄
* 각 패치들에 대해 softmax 결과를 평균화

#### PCA
* 이미지의 각 RGB 픽셀에 PCA를 적용하여 평균=0, 표준편차=0.1을 갖는 랜덤 변수를 곱한 뒤 기존 픽셀에 더해줌

### Dropout
각 뉴런들의 출력결과를 0.5의 확률로 0으로 만드는 것
*  0이 된 뉴런은 forward pass시나 backpropagation시에 전혀 기여하지 않음
*  뉴런간의 상호의존성을 없애므로 모델이 더 robust
*  Test시에는 모든 뉴런들을 사용하지만 각각 0.5를 곱해준다. 

## Details of learning

* optimizer : Stochastic Gradient Descent(SGD) + momentum(0.9)
* batch size : 128
* weight decay : 0.0005 
  > 정규화 뿐만 아니라 training error를 줄여줬음
* lr : 0.01, 모든 layer에 동일한 lr 적용
* epoch : 90

## Results

<p align="center"><img width="407" alt="스크린샷 2022-10-12 오후 11 52 24" src="https://user-images.githubusercontent.com/56713634/195382209-b2abce4f-6450-4feb-bb0c-6d1daa543de0.png"><p>

> ILSVRC-2010 대회 때의 모델들과 CNN을 사용한 AlexNet을 비교한 결과

> sparse coding은 6개의 sparse-coding model들로부터 나온 predict 결과를 평균하여 예측하는 방식

> SIFT + FVs 는 Fisher Vectors(FVs)로부터 훈련된 두 개의 분류기로 predict한 것들의 평균으로 예측하는 방식

<p align="center"><img width="627" alt="스크린샷 2022-10-12 오후 11 52 31" src="https://user-images.githubusercontent.com/56713634/195382526-7b0dafaa-c160-431f-84f3-0aa79c7b98e6.png"><p>

> ILSVRC-2012 대회 때 AlexNet(CNN)을 적용한 결과

> 1 CNN은 CNN모델을 하나 썼을 경우이고, 5 CNN은 5개의 CNN모델을 사용하고 그 평균을 사용하여 예측했을 때의 결과

> 1 CNN*은 하나의 CNN모델에 추가로 6개의 convolutional layer를 붙인 모델
  > ImageNet Fall 2011데이터(1500만개의 이미지, 22000개의 카테고리)로 훈련을 한 뒤, ILSVRC-2012로 fine-tuning한 결과

> 7 CNNs*는 1 CNN* 7개의 모델을 돌려 그 평균을 사용하여 예측한 결과


### Qualitative Evaluations
신경망내 2개의 데이터가 연결되는 계층에서 합성곱 kernel을 보여줌

<p align="center"><img width="396" alt="스크린샷 2022-10-13 오전 12 12 22" src="https://user-images.githubusercontent.com/56713634/195382099-0095e94b-ec7d-4585-b062-0ddeb034823d.png"><p>

* 첫 번째 GPU에서는 color가 거의 인코딩되어 있지 않지만, 두 번째 GPU에서는 color가 인코딩되어 있는 모습을 확인 가능

<p align="center"><img width="940" alt="스크린샷 2022-10-13 오전 12 06 12" src="https://user-images.githubusercontent.com/56713634/195381920-e392fe8f-0f63-4b2e-b21b-903e30d7582f.png"><p>

#### 왼쪽이미지
* 빨간 그래프가 정답 레이블에 해당하는 그래프
* 위치에 상관없이 잘 분류함을 확인할 수 있음

#### 오른쪽이미지
* 좌측 사진은 가장 왼쪽의 column이 test set에서 뽑은 것들이고, 나머지는 train set에서 뽑은 이미지들이다
* Test set에서 뽑은 사진들을 각각 모델에 넣고, 4096-layer에서의 feature activation을 기준으로 가장 근사한 것들을 뽑은 것
* 픽셀 단위로는 test set과 train set이 전혀 다르지만(색이나 포즈라던가), 그럼에도 불구하고 같은 부류라고 판단함을 확인 가능

## Discussion
* 지도학습만으로 크고 깊은 CNN이 방대한 데이터셋을 분류하는데에도 뛰어난 성과를 보임
* 하나의 합성곱계층만 제거해도 결과가 나빠짐을 확인했다.
> 예를 들어, 중간에 하나의 계층만 제거해도 top-1 에러율이 2%가 나빠진다. 그렇기에 깊이 또한 우리의 결과에 매우 중요하다.
* 충분한 컴퓨팅 파워가 있다면 네트워크의 사이즈(깊이)를 더 늘림으로써 더욱 뛰어난 성능을 발휘할 것이다.
