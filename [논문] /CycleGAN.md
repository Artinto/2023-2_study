# CycleGAN
## Abtract
<img width="943" alt="image" src="https://github.com/Artinto/2023-2_study/assets/127365253/44c1c724-a836-4eae-aa2e-75116be2a9aa">

### GAN
<img width="800" alt="image" src="https://github.com/Artinto/2023-2_study/assets/127365253/b4d04bed-1948-41ac-877e-8b858c1047a8">

  
* 생성자(generator)와 판별자(discriminator) 두 개의 네트워크를 활용한 생성 모델  
* 목적 함수(objective function)를 통해 생성자는 이미지 분포를 학습할 수 있다

### CGAN (조건부 GAN)
<img width="800" alt="image" src="https://github.com/Artinto/2023-2_study/assets/127365253/d480988c-a144-47cc-8330-95a3f1915d8b">  


입력을 줄 때 조건 벡터인 Y를 같이 준다 -> Y : 일반적으로 Label 과 같은 모든 정보를 제어할 수 있는 Dataset  
이때 Y는 꼭 class가 아니더라도 어떠한 조건의 정보를 줄 수 있을 때 적용시킬 수 있다  

### Pix2Pix
Pix2Pix는 학습 과정에서 이미지 X 자체를 조건(condition)으로 입력받는 cGAN의 한 유형  
픽셀(pixel)들을 입력으로 받아 픽셀(pixel)들을 예측한다는 의미를 가진다  
<img width="800" alt="image" src="https://github.com/Artinto/2023-2_study/assets/127365253/8da8f266-6a83-4b7a-be07-8ff208b51eaf">  
한 쌍의 dataset을 사용 -> 정답을 알고 있는 dataset에서만 적용 가능 

<img width="700" alt="image" src="https://github.com/Artinto/2023-2_study/assets/127365253/8e7f4846-85f1-42e2-bd59-e0b9b26beee6">  

GAN의 성능을 더 향상시키기 위해 L1 손실(loss) 함수를 함께 사용한다  
* L1 손실을 이용했을 때 흐림(blurring)현상이 덜 발생  

<img width="800" alt="image" src="https://github.com/Artinto/2023-2_study/assets/127365253/ed05ec73-9ab9-4182-9c37-0a0d851791bf">  

두 개의 loss를 적절히 섞어 사용할 때 그러한 artifact가 적으면서도 우수한 결과가 나오는 것을 확인할 수 있다  


Pix2Pix의 한계점  
* Pix2Pix는 서로 다른 두 도메인 X,Y의 데이터 두 개를 한 쌍으로 묶어 학습을 진행한다
  -> 즉, Paired한 데이터가 아닌 Unpaired한 데이터에서 적용 부적합
  -> 이를 CycleGAN을 이용해 해결 가능

## Introduction

<img width="589" alt="image" src="https://github.com/Artinto/2023-2_study/assets/127365253/1de8309b-8d69-4c1c-9523-c7cd45bee7c8">  

같은 이미지에 대해 2개의 특성을 갖는 이미지 쌍은 구하기가 쉽지 않다  
Cycle-GAN은 이런 pair-image를사용하지 단지 X도메인 데이터세트와 Y도메인 데이터세트만을 이용해 두 도메인 간에 이미지를 변환하는 법을 학습한다  


<img width="800" alt="image" src="https://github.com/Artinto/2023-2_study/assets/127365253/5aba65f3-4201-4ad7-8702-00aad38d6e97">  

이때 GAN LOSS만을 사용한다면, G는 어떤 입력이든 Y 도메인에 해당하는 하나의 이미지만 제시할 수도 있다  
다시 말해 x1의 content 정보를 아예 변경해 버릴 수 있기 때문에, 추가적인 제약 조건이 필요하다  

## Method  

<img width="147" alt="image" src="https://github.com/Artinto/2023-2_study/assets/127365253/742118dc-f5e4-41f1-b94d-d6a995125d71">

CycleGAN은 G(x)가 다시 원본 이미지 x로 재구성(reconstruct)될 수 있도록 한다  
1. 2개의 변환기(translator)를 사용   
* G: X -> Y
* F: Y -> X
(G와 F는 역함수 관계)

2. 원본 이미지가 다시 복원될 수 있도록 cycle consistency loss를 사용

<img width="604" alt="image" src="https://github.com/Artinto/2023-2_study/assets/127365253/adef0d5b-4b0f-4eb5-a324-df76fb33b1d6">


<img width="806" alt="image" src="https://github.com/Artinto/2023-2_study/assets/127365253/e18e7118-22e8-4579-bbc9-5192d6c6052e">  

* Ganloss : target domain의 있을 법한 이미지를 생성하게 하는 loss
* Cycle-consistent loss : 입력과 매칭되는 image-to-image translation 결과 이미지를 찾을 수 있도록 하는 loss

## Architecture  
* 학습방법(Traning details)
    * Least-squares loss : 기존의 cross-entropy 기반의 loss 대신에 MSE 기반의 loss 사용
      -> 실제 이미지 분포와 더욱 가까운 이미지를 생성할 수 있으며 학습이 안정화된다
    * Replay buffer : 생성자가 만든 이전 50개의 이미지를 저장해 두고, 이를 이용해 판별자 업데이트
      -> 모델의 oscillation 개선

## Result  

<img width="414" alt="image" src="https://github.com/Artinto/2023-2_study/assets/127365253/7a594385-3811-4a37-98e1-77c404edc55c">



