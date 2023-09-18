# SRGAN
## Abstract  
### SRCNN
Image Super-Resolution은 저해상도 이미지를 고해상도로 변환시키는 문제를 의미한다  
* 미디어, 의료, 보안 등 다양한 산업 분야에서 중요한 문제로 대두되고 있다

  <img width="652" alt="image" src="https://github.com/Artinto/2023-2_study/assets/127365253/312d3cde-4f2f-4a12-957f-b406dac590fc">  
  
  Computer Vision 영역에서 좋은 성능을 보이고 있는 다양한 딥러닝 모델을 적용해 Image Super-Resoltion 문제를 해결하려는 연구가 다수 진행되고 있다
  
SRCNN PROBLEM
1. 저해상도 이미지와 고해상도 이미지 크기가 다른 문제를 어떻게 다룰 것인가?
   <img width="689" alt="image" src="https://github.com/Artinto/2023-2_study/assets/127365253/5f7626b9-4363-406b-82d2-2a1dade65154">

   -> Interpolation, Transpose convolution, Sub-pixel convolution 등으로 Upsampling 진행
   * Nearest-neighbor interpolation
     <img width="680" alt="image" src="https://github.com/Artinto/2023-2_study/assets/127365253/b7b24866-019e-4797-b726-a6b903666cf4">
     * Interpolation 방법 중에서 가장 간단한 방법
     * 빈 픽셀은 가장 가까운 픽셀 값으로 채우는 방법  
    모델 내에 Upsampling을 하는 위치에 따라 다양한 Framework가 존재
    연구에 따라 Upsampling 방식을 다양하게 적용할 수 있음
    <img width="664" alt="image" src="https://github.com/Artinto/2023-2_study/assets/127365253/ae5e3ea4-7c41-4d7a-a57a-ea20081ce736">


2. Image Super-Resoltion 문제에 대해 어떻게 딥러닝 모델을 적용할 것인가?  
   -> 일반적인 분류, 회귀 모델에서 사용하는 모든 방법론이 적용 가능함
   
   <img width="691" alt="image" src="https://github.com/Artinto/2023-2_study/assets/127365253/5c204249-ef18-480f-b4f1-25cf7bbe88c8">

   
## Introduction  
논문이 발표된 2017년을 기준으로 SR분야에서는 CNN이 다양하게 활용되고있다  
하지만 공통적으로 Upscale Factor가 큰 경우에는 미세한 질감(finer texture details)을 복구하는데 어려움이 있다는 문제점을 가지고 있다  
-> 기존 모델들이 사용하는 목적함수(objective function)이 원인  
   초기 SRCNN을 비롯한 대부분의 모델이 목적 함수로 MSE를 채택하였다  
   * MSE란?  
     평균제곱오차(Mean Squared Error, MSE)는 이름에서 알 수 있듯이 오차(error)를 제곱한 값의 평균이다
     MSE를 계산하고 그 값을 줄여가기 위해 세타를 변경해가며 오차를 줄여간다
     
MSE 기반 학습의 문제점 : 사람의 지각적 감각을 재현하지 못한다  
<img width="389" alt="image" src="https://github.com/Artinto/2023-2_study/assets/127365253/0349a5e0-1837-49a3-a90b-285748583f32">  
MSE는 같은 위치의 픽셀끼리의 값의 차이를 구한다 따라서 모델은 같은 위치의 픽셀에 다른 정보가 들어가 있기 때문에 평행 이동을 한 두 이미지의 해상도가 전혀 다르다고 판단한다  
그래서 MSE를 활용하여 SR 모델을 학습하면 스무딩(Smoothinf)현상이 발생한다  

## Method  
[1] 새로운 아키텍처 : GAN(Generative adversial network)을 활용한 SR모델 , SRGAN  

GAN을 활용하여 4x Upscaling이 가능한 최초의 Framework를 구현했다  
GAN은 원본 이미지와 유사한, '그럴듯한'이미지를 생성하는데 특화가 되어 있는 모델이다  
진짜와 가짜를 구분하는 판별자를 속이기 위해 생성자는 원본 이미지의 데이터 공간쪽으로 점점 접근하여 특징을 탐색한다  
그래서 SR 분야에 GAN을 활용하면 원본 이미지의 미세한 질감을 잘 보존한 고해상도 이미지를 만들 수 있다는 장점이 있다  

[2] 새로운 손실 함수: 지각적 손실 함수(Perceptual Loss Function)  

지각적 손실 함수는 사람이 느끼는 고해상도 이미지와 가까워지기 위해 고안된 손실 함수  
Adversarial Loss와 Content Loss의 가중치 합으로 구성된다  
* Adversarial loss  
  GAN에서 생성자의 LOSS
* Content loss  
  MSE의 Pixel 단위의 유사성을 지각적 유사성으로 대체하기 위해 제안된 손실 함수이다
  생성자가 만든 가짜 고해상도 이미지와 진짜 고해상도 원본 이미지를 사전 훈련된 모델에 통과시키면 최종 결과물로 Feature Map을 얻게 된다  
이 두 Feature Map 간의 차이를 구하는 것이 바로 Contene Loss이다

따라서 Adversarial Loss와 Content Loss의 가중치 합으로 구성된 지각적 손실함수는 실제 고해상도 이미지 데이터 공간 근처에서 원본 표현을 잘 따라하는 SR이미지를 만들 수 있게 도와주는 함수  

학습 데이터 구성하기  
SR분야의 목적은 저해상도 이미지로부터 고해상도 이미지를 추정하는 것  
따라서 학습에는 (저해상도, 고해상도) Paired한 이미지가 필요  

저해상도 이미지는 고해상도 이미지에 가우시안 필터(Gaussian filter)를 적용한 다음 가로, 세로를 r배 (Downsampling factor) 줄임으로써 얻을 수 있다  
워논 고해상도 이미지의 크기가 rW x rH x C라고 한다면, 생성된 저해상도 이미지의 크기는 W x H x C가 된다  

SRGAN 목적 함수  
<img width="398" alt="image" src="https://github.com/Artinto/2023-2_study/assets/127365253/637ee2b6-e79f-43bc-92db-1df40667f4e4">  
일반적으로 GAN에서는 진짜는 1로, 가짜는 0으로 정의한다  
이상적인 판별자는 진짜 이미지를 진짜, 1로 판단해야한다 따라서 진짜 고해상도 이미지가 판별자에 입력되면 log(1)=0이 돼야 한다  
반대로 가짜 이미지는 가짜, 0으로 판단해야 한다 -> log(1-0) = 0 따라서 판별자는 최댓값이 0인 목적함수를 0에 가까워지도록 최대화해야 한다  

<img width="398" alt="image" src="https://github.com/Artinto/2023-2_study/assets/127365253/2fd1d498-54c0-45eb-8d5a-ac6dab118e78">  

다음으로 생성자의 목적함수를 살펴보면 생성자의 목표는 Content Loss와 Adversarial Loss의 가중치 합으로 구성된 지각적 손실 함수를 최소화하는 것이다  

<img width="362" alt="image" src="https://github.com/Artinto/2023-2_study/assets/127365253/dafd6815-b0bc-414c-9e40-005851ec2c91">  

먼저 생성자의 Adversial Loss는 일반적은 Gan에서의 생성자의 Loss 함수 공식과 동일하다  
형태를 보면 판별자의 목적 함수에서 뒷부분만 차용한 형태이다  
생성자는 진짜 같은 가짜 이미지를 만드는 것이 목표이므로 판별자의 목적 함수에서 앞 부분은 필요가 없다  

<img width="399" alt="image" src="https://github.com/Artinto/2023-2_study/assets/127365253/a4c853c7-191c-4bff-8080-cd542b50ef13">   

다음으로 Content Loss이다  
SRGAN에서 생성자의 목적함수에 추가된 특별한 공식이다  
생성자가 생성한 가짜 이미지와 원본 진짜 이미지를 사전 학습된 VGG19 모델에 통과 시킨다  
-> 활성함수 ReLU Layerㄹ를 통과하고 Max-Pooling Layer을 통과하기 전까지  
그러면 각각 Feature Map들을 얻을 수 있다  
Content Loss는 이들 Feature Map 끼리 MSE이다. 공식을 잘 보면 Feauter Map 끼리 element-wise 연산 후 제곱하여 전체 원소의 개수로 평균을 구하는 형태인데 이는 MSE의 공식과 동일하다  
기존 이미지는 가짜 이미지와 실제 고해상도 이미지를 직접 비교하여 MSE를 구했다면, Content Loss는 간접적으로 Feature Map 끼리의 MSE를 구하는 셈이다  

<img width="385" alt="image" src="https://github.com/Artinto/2023-2_study/assets/127365253/8377edfb-10f4-490d-9e74-aefdc027b6a2">  

빨간색 박스가 Max Pooling Layer이다  
Content Loss는 빨간색 박스를 통과하기 직전의 Feature Map을 활용하여 값을 산출한다  
어디까지 통과시킬지는 본인의 선택이지만 논문에서는 마지막 Pooling Layer 바로 직전까지 통과시킨 Feature Map을 활용하는 게 가장 성능이 좋다고 한다  

# Experiments  
MOS로 모델의 성능을 비교 평가  
사람의 지각적 능력을 기준으로 모델의 성능을 평가하기 위해 26명의 평가자가 SR이미지에 1점부터 5점까지 점수를 부여한다  
1점은 Bad Quality를 의미하고 5점은 Excellent Quality를 의미  
NN, SRCNN과 같은 오래된 모델부터 SRGAN-VGG54 까지 총 12개의 다른 모델에 대해 MOS 성능 평가를 진행한다  

<img width="411" alt="image" src="https://github.com/Artinto/2023-2_study/assets/127365253/025bdbec-26a8-4c9f-a0cb-dc0ee1cedef2">  

MOS 점수를 보면 역시 SRGAN 평가가 가장 높은 것을 확인할 수 있다. 다만, 아직 원본 이미지의 수준에는 접근하지 못한다는 한계가 있다  













     

   
   
   

     
     
