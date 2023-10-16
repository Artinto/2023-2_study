# StyleGAN
## 순서
- PGGAN
  -  [Progressive Growing of GANs for Improved Quality, Stability, and Variation (2018)](https://arxiv.org/abs/1710.10196)
- StyleGAN
  - [A Style-Based Generator Architecture for Generative Adversarial Networks(2019)](https://arxiv.org/abs/1812.04948)
- StyleGAN2
- StyleGAN3

## Introduction
- 이미지 생성에서 스타일과 특징의 독립적인 조절을 가능하게 하는 GAN
- PGGAN 구조에서 Style transfer 개념을 적용하여 generator architetcture를 재구성 한 논문

## PGGAN
![image](https://raw.githubusercontent.com/happy-jihye/happy-jihye.github.io/master/_posts/images/gan/pggan1.gif)
- PGGAN, ProGAN, PGAN, Progressive GAN 등 다양한 이름으로 불리는 GAN
- StyleGAN의 시초
- 저해상도 사진에 layer를 추가하며 학습하여 고해상도의 사진을 생성하는 모델

### Progressive training
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/be25f5f6-4df9-4a41-b9d3-34854751c84d)
- 일반적으로 high-resolution(고해상도) 생성이 어려워 D가 가짜를 쉽게 구별함
- 만들기 쉬운 low-resolution(저해상도) 이미지를 생성하고 점진적으로 layer를 증가시키며 세부 사항을 추가하여 high-resolution 이미지를 생성함
- image distribution에서 큰 구조(coarse-grained)의 특징을 우선적으로 학습
- 점차 세말한 특징(fine-grained)들을 이어서 학습
- 장점
  - stable: 저해상도 사진은 class information도 적고 mode도 몇 없기 때문에 학습 초기에는 low-resolution 학습이 더 안정적
  - Reduced training time: 학습 시간 단축 (최대 6배 단축)
- 단점
  - latent vector인 z가 Normalize를 거친 후에 바로 생성자(Generator)에 입력으로 들어감
  - latent space의 entanglement(얽혀있음) 문제를 유발

## Entanglement, Disentanglement
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/a43a5978-d622-4310-bb76-38ccc29aea72)
- (a) : 이상적인 latent space
  - linear한 attrubute
- (b) : 기존의 generator ( PGGAN )
  - entangle 된 상태
  - style(특징)이 서로 상호작용 하여 영향을 미침
- (c) : disentangle한 latent space
  - W를 이용하여 각 특성의 변화를 linear하게 조절할 수 있게 됨
  - W(Linear Transformation)는 입력 벡터를 행렬과 벡터의 곱셈으로 변환하는 것을 의미
  - 표정, 머리 스타일, 머리카락 색상 등을 각각 다르게 제어

## Style-based Generator
- Generator에 latent vector z가 바로 입력되게 때문에 entangle하게 되어서 불가능 하다는 단점을 해
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/2f6e4b80-052b-441d-b011-fd70e109be6a) 
- Traditional Generator
  - latent vector(잠재 벡터)가 normalize(정규화) 되는 구조
  - training data가 latent space(잠재 공간)의 probability density(확률 밀도)를 따라야 하기 때문에 entanglement하게 됨
  - 즉 실제 데이터와 유사한 이미지만을 만들기 때문에 원하는 방향이 아닌 결과가 생성될 수 있음
- Style-based Generator
  1. Mapping Network
     - latent vector z를 중간 latent space W의 스타일 코드로 매핑(변환)하는 역할
     - 중간 latent space W를 사용함으로써, 이미지 스타일과 특징을 독립적으로 조절
  2. Synthesis Network
     - 중간 latent space W의 정보를 활용하여 이미지를 생성하는 역할
     - 중간 latent space의 스타일 코드와 이미지 특징을 조합하여 다양한 스타일의 이미지를 생성
     - 이미지 생성의 예측 가능성과 다양성을 높이는 데 도움을 줌
    
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/9a33f489-fd94-4c70-82e3-2f7d177321f1)  
## mapping network
- mapping network는 8-layer MLP로 구성
- 512차원 z를 512차원 w로 mapping해주는 역할  

**Z (잠재 공간 Z)**  
- 정규분포(Gaussian)를 따르는 잠재 벡터(벡터 형태의 숫자) 공간
- Z 내의 값은 무작위로 샘플링되며 이미지 생성에 무작위성을 주입하기 위해 사용
- 주로 이미지 생성의 난수 초기값으로 활용되며, 초기에는 무작위한 이미지를 생성합니다.  

**W (중간 잠재 공간 W)**
- 매핑 네트워크(Mapping Network)를 통해 변환된 스타일 코드(Style Code)를 담는 공간
- 이미지 스타일 및 특징을 표현하고 제어
- 각 차원은 이미지의 특정 특징 또는 스타일을 나타냄
### 정리  
- Z는 초기 무작위 벡터로부터 시작하여 이미지 생성을 위한 무작위성과 다양성을 제공하는 공간
- W는 이미지의 스타일과 특징을 조절하고 제어하는 중간 공간
- W는 Z를 더 구조적이고 예측 가능한 방식으로 변환하여 이미지 생성의 예측 가능성과 다양성을 향상시키는 역할

## synthesis network
- 4x4부터 1024x1024 resolution feature map을 만드는 총 9개의 style block으로 구성
- 마지막에는 RGB로 바꿔주는 layer
- style block의 input은 이전 style block의 output인 featuremap
- style block당 두번의 convolution을 진행

### Style Modules (AdaIN-Adaptive Instance Normalization)
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/fdf0472d-ee2b-4f55-a313-d4518f3b7042)
- content 이미지 x에 style 이미지 y의 스타일을 입힐 때 사용하는 normalization
- style transfer를 하는 경우 꼭 필요한 단계
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/974b9239-0697-47ca-b1ac-41ee2bf303fe)
- 입력 이미지의 각 채널 또는 특성 맵의 스타일을 학습
- 다른 이미지에 이 스타일을 적용
- 이미지 스타일 전이나 변형을 가능하게 하며, 스타일과 콘텐츠를 분리하여 이미지 스타일을 변경하거나 특정 스타일로 이미지를 적용하는 데 사용
- 구조
  - Content 이미지 정규화
    - 스타일을 적용하고자 하는 대상을 정규화
  - Affine Transform
    - 스타일 변형을 얻기 위해 Affine Transform(이동 및 확대/축소)를 수행
  - Style Scaling Factor σ(y)와 Style Bias Factor μ(y)
    - Affine Transform을 통해 스타일 이미지에서 스케일링 요소(σ)와 바이어스 요소(μ)를 추출
    - 스타일의 크기와 이동을 나타내는 요소
  - Scaling
    - 스타일 이미지에서 얻은 스케일링 요소와 바이어스 요소를 적용하여 변형
    - Content 이미지가 스타일 이미지의 스케일과 이동에 맞게 조절됩니다.
- Content 이미지에 스타일을 적용하여 다른 스타일을 가진 Style 이미지를 생성할 수 있음

### Constant Input
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/e30b4e76-400f-4abd-97c5-1b3c49ab2a50)
- synthesis network는 4x4x512 contant tensor에서 부터 시작
- w를 입력으로 받기 때문에, PGGAN과 같이 z에서 convolution연산을 하지 않아도 됨
- random한 noise에서 시작하는 것보다 contant에서 시작하는 것이 더욱 성능이 좋음
- disenstangle한 w를 사용하기 때문에 entangle된 z를 사용하는 것을 피하는 효과 때문이라고 예상 (특징과 스타일이 서로 분리)

### Stochastic Variation (확률적 변화)
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/3f99b407-85d3-4de0-8dd4-fe942469d4df)
- 머리카락의 배치이나 모공, 주근깨 같이 아주 세밀하고 때에 따라 달라지는 특징 (Stochastic Variation)
- 세부적인 attribute를 추가하기 위해 Noise를 추가하여 이미지의 다양성을 증가시키는 부분
- Gaussian에서 sampling한 nosie를 Convolution의 output인 featuremap에 더해줌
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/008087d7-6afa-4e5f-99fc-7890b76fd34d)

## Properties of the style-based generator
### Style Mixing
- 하나의 w로 학습을 하면 발생하는 correlation 문제를 해결하기 위해 style을 섞는 것
- latent code 2개를 sampling (z1, z2)한 후, mapping network를 거쳐 2개의 style code(w1, w2)를 만드는 것
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/b83ba643-6605-49ce-90a1-b0daacd777f7)

- single Latent z를 이용할 경우
  - 동일한 latent vector z가 Mapping network f를 통해서 나온 W 하나만 계속 네트워크를 학습
  - 데이터셋에서 우연하게 대머리인 사람들이 항상 선글라스를 끼는 경우
    - 대머리 == 선글라스라는 correlation 발생
- multi Latent z를 이용할 경우
  - latent vertor z1, z2, z3 등이 Mapping network f를 통해서 w1, w2, w3 등을 생성
  - 각 layer에 나눠서 적용
  - 세밀한 부분들을 나누어서 학습 가능
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/1e9e96bd-a523-4145-8454-22261177cb38)

