# SNGAN  
## Abstract  
GAN 학습에 있어 훈련의 불안정성을 해결할 수 있는 새로운 방법 필요  
* 불균형한 학습  
  초기에 판별자와 생성자의 성능 차이가 매우 큰 경우 판별자는 쉽게 가짜와 진짜 데이터를 구별할 수 있다  
  -> 생성자는 거의 어떠한 피드백도 받지 못하고 생성하는 이미지가 제한적일 수 있다
* 모드 붕괴  
  생성자가 제한된 이미지나 패턴만 생성하도록 수렴하는 현상
  -> 판별자가 특정모드에 대해 민감하게 반응하고 나머지 모드에 대해서는 무시할 때 발생
  -> 생성자가 판별자가 약한 모드를 피하기 위해 그 모드에 대해서만 생성하는 이미지를 생성하는 문제가 발생
  
이에 discriminator의 훈련을 안정화시킬 수 있는 spectral normalization을 새롭게 제안  
이를 통해 계산량이 줄어들고 쉽게 적용할 수 있으며 학습의 안정성을 강화시킴  
더 효과적인 성능을 증명하기 위해 여러가지 실험을 토대로 증명함  

## Introduction  
Gan이 학습이 쉽지 않은데, 이 논문에서는 discriminator의 좋은 학습을 위해 stablize한 학습 방법을 제안함  
우리가 학습시키는 parameter의 weight를 normalize하는 방식 -> spectral normalization  
Lipschitz constant를 제약하는 방식으로 진행됨 -> 원래 있던 기존의 방식보다 쉬운 implementaion만으로도 접근이 용이하다는 특징이 있다  

* Lipschitz 함수란?
  
  <img width="659" alt="image" src="https://github.com/Artinto/2023-2_study/assets/127365253/ff77ba0a-447d-4e8f-bb1e-1734209e5494">  
  
  어떠한 함수 f:[a,b] -> R 가 어떠한 상수 M과 [a,b]에 속하는 모든 x,y에 대해서 이 식을 만족하게 만든다  
  다시 말해 **두 점 사이의 거리를 일정 비 이상으로 증가시키지 않는 함수** 라고 정의할 수 있다  
  -> f의 미분계수가 M을 넘어가지 않는다는 것으로 해석 가능 
## Spectral Normalization    
GANs is given by  

<img width="123" alt="image" src="https://github.com/Artinto/2023-2_study/assets/127365253/5be589f7-f9c5-4f07-bd6c-c543f3e76fa8">

<img width="493" alt="image" src="https://github.com/Artinto/2023-2_study/assets/127365253/fe3cb635-2846-4a20-a7ba-d2ab002cd302">  


-> derivative  
<img width="312" alt="image" src="https://github.com/Artinto/2023-2_study/assets/127365253/b1b0cce2-7dea-49f9-9680-13456a11b3f6">  
GAN에 있어 최적의 Discriminator는 위와 같이 표현할 수 있다  

$sigmoid(x)=1/1+e^{-x}$ 이기 때문에 f*를 sigmoid에 넣어 풀면 DG*와 같이 가능하다  
하지만 여기서 보듯이 generate 미분값에 대한 어떠한 제약조건이 없는 것을 알 수 있다  
새로운 제약을 걸어주면 더 좋은 학습을 시킬 수 있지 않을까 라는 아이디어 제시  

이 논문이 나오기 전 제약을 걸어주기 위한 새로운 방법들 제기  
* WGAN  
  discriminator가 아무 함수나 학습할 수 없게 Lipschitz constant를 걸어 좋은 함수를 학습시킨다는 아이디어  
  <img width="198" alt="image" src="https://github.com/Artinto/2023-2_study/assets/127365253/73d3c490-3989-4305-aa66-4524c97dae8a">  
  wight clipping  
  <img width="282" alt="image" src="https://github.com/Artinto/2023-2_study/assets/127365253/55d98b47-0ba0-49db-96f7-ed4dd17d960b">  
  각각의 parameter가 어떠한 값 이상으로 넘어가지 않게 강제적으로 막아놓는 방법  
  한계 : 위의 그래프처럼 전체적으로 좋은 함수가 학습된다기 보단 간신히 넘어가려는 함수만 급하게 막는 식으로 밖에 진행이 안됨

* GAN-GP (Gradient Panalty)
  
  <img width="318" alt="image" src="https://github.com/Artinto/2023-2_study/assets/127365253/71a83bce-f82a-499a-bacb-2ad96302d9b5">  
  
  generate의 model의 datasample 하나와 real image의 datasample 하나를 각각 뽑아 그 두 사이의 gradient를 구한다  
  이 하나의 기울기를 regulation에 넣는다
    
  -> 실제의 기울기를 넣은 것이기 때문에 위에 설명한 WGAN보단 더 효과적인 학습이 가능함  
  한계 : sample 하나를 뽑아서 학습을 진행하기 때문에 그 sample에 가까운 한정적인 영역안에서는 regulation이 걸리고 나머지의 영역에서는 regulation이 제대로 걸리지 않는 문제가 발생

* Spectral Normalization  
  각 layer의 g의 spectral norm을 제어함으로써 discriminator 함수 f의 Lipschitz constant를 제어하는 것
  
  "Matrix Norm"
  유클리드 거리

  ![image](https://github.com/ces0o/Paper-Review/assets/127365253/f8fa2f1b-7ee5-4828-8c12-4b771b8bf754)

  수학에서는 유클리드 거리를 계량하는 함수를 노름(norm)이라 한다
  이 노름의 치역은 음이 아닌 실수로 정의한다
  노름 개념이 벡터에 쓰이면 벡터 노름, 행렬까지 확장하면 행렬 노름(matrix norm)이라 한다
  노름은 거리를 일반화하기 때문에 표기법도 유클리드 거리와는 달라진다

  ![image](https://github.com/ces0o/Paper-Review/assets/127365253/740e3623-9bf4-4c44-aca2-6dee341e45d3)

  제곱과 제곱근을 사용한 유클리드 노름을 더 일반화해서 정의한 p-노름도 있다

  ![image](https://github.com/ces0o/Paper-Review/assets/127365253/fb288813-e18b-428f-97bc-a42473ea640a)

  ![image](https://github.com/ces0o/Paper-Review/assets/127365253/532c35d3-a3c6-413d-a9da-ac751f187922)

  연립방정식 $Ax=b$ 에 등장하는 행렬의 곱 $Ax$ 를 이용해서 행렬을 벡터로 바꾼 후 행렬 노름을 다음과 같이 정의한다

  ![image](https://github.com/ces0o/Paper-Review/assets/127365253/5c32e7dd-e19c-437a-b9dd-14071961974d)

  여기서 x는 임의의 모든 열 벡터이다
  열 벡터에 따라 벡터 노름은 달라지므로 행렬 A가 x를 기준으로 Ax를 최대로 증폭하는 비율로써 행렬 노름을 정의한다
  또한 행렬 노름은 벡터 노름을 바탕으로 정의하르모 p-노름을 강조해서 다음처럼 식을 쓸 수 있다

  ![image](https://github.com/ces0o/Paper-Review/assets/127365253/e89abee6-1157-4d45-a0e6-65e0d7162b57)

  ﻿spectral normlization은 각 layer g : h(in) -> h(out)의 spectral norm을 제한하는 것으로 discriminator function f의 lipschitz constant를 조절한다
  정의에 따라 Lipschitz norm ![image](https://github.com/ces0o/Paper-Review/assets/127365253/b6d2fccc-b808-400c-8929-4410f4824674)은 ![image](https://github.com/ces0o/Paper-Review/assets/127365253/46497ae7-013c-4ed6-96fd-b874d7f04776)와 동일한데 여기서 ![image](https://github.com/ces0o/Paper-Review/assets/127365253/acc7bf56-dff6-464f-b344-4f66926da848)는 matrix A의 spectral norm이다 (L2 matrix norm of A)

  ![image](https://github.com/ces0o/Paper-Review/assets/127365253/27b57dc1-a958-45d2-8879-848f419ea80a)

  이는 A의 largest singular value와 동일하다
  따라서 linear layer g(h)=Wh에 대해 norm은

  ![image](https://github.com/ces0o/Paper-Review/assets/127365253/d6253ac8-0b6c-48c4-b3c1-60def1e77578)

  로 주어진다
  
  ![image](https://github.com/ces0o/Paper-Review/assets/127365253/669aa8bc-65c4-488d-b5eb-569d0c50c566)는 input x를 넣었을 때 neural network에 의해 만들어지는 discriminator로 다음과 같은 식으로 정의 될 수 있다

  ![image](https://github.com/ces0o/Paper-Review/assets/127365253/200815c3-f613-4428-afa0-35783d9b0077)

  여기서 a(L)은 activation function을 의미한다 만약 a의 lipschitz의 값이 sigmoid와 같이 1이라면 다음의 식을 적용할 수 있다

  ![image](https://github.com/ces0o/Paper-Review/assets/127365253/b32a0671-d17b-4eb2-bddb-417369cebf5a)

  이 식을 앞에 정의한 함수 f에 적용시키면

  ![image](https://github.com/ces0o/Paper-Review/assets/127365253/c0e571b3-60b5-4692-9b97-1485a2a9ccc7)

  이러한 식으로 되고 결국은 F의 lipschitz의 bound를 찾을 수 있다
  spectral normlization은 wight matrix W의 spectral norm을 normalize하여 lipschitz constraint ![image](https://github.com/ces0o/Paper-Review/assets/127365253/2ce7b3d4-992a-46ff-a5db-2f3d83942b05) =1을 만족하게 된다

  ![image](https://github.com/ces0o/Paper-Review/assets/127365253/eba0c621-be64-44c0-9385-f853a53ec6d9)

  이러한 식으로 각 W(l)을 normalize하게 되면 ![image](https://github.com/ces0o/Paper-Review/assets/127365253/70f325b2-904f-4a4d-baff-09c7cda4f9bf)  라는 사실에 의해 ![image](https://github.com/ces0o/Paper-Review/assets/127365253/ca144eb4-c85e-49cf-9c8a-fb3ee49370fc) 가 1로 bound 됨을 알 수 있다
  discriminator의 각 layer을 regularize하기 위해 사용한 spectral norm은 W의 largest singular value이 된다

  ![image](https://github.com/ces0o/Paper-Review/assets/127365253/801859cb-6f5c-445b-865b-c09a582dae0a)에 대한 계산을 위해 singular value decompostion(SVD)를 진행할 시 계산량이 너무 많다
  따라서 power interation method를 통해 ![image](https://github.com/ces0o/Paper-Review/assets/127365253/35cd8134-246d-4c50-983f-6cf53e6606e0)를 추정하는 것이 더 효율적이다

* Gradinet Analysis of the Spectrally Normalized Weights

  ![image](https://github.com/ces0o/Paper-Review/assets/127365253/8d8f26a6-cfd1-4a4d-a8bd-1d1526c56aa7)

  이 식은 위의 W(SN)식을 한 번 미분한 결과 값이다

  ![image](https://github.com/ces0o/Paper-Review/assets/127365253/db717e51-0ce6-4079-831e-36dad520db1a)

  이 식은 chain rule에 의해 미분을 한 값이고 그 결과 값이 위의 식과 비슷한 형태를 띄는 것을 알 수 있다
  따라서 위의 식을 이 식에 대입을 해주면

  ![image](https://github.com/ces0o/Paper-Review/assets/127365253/6b0a1687-108f-4621-8fbc-1d67a22caaa9)

  이러한 식이 완성된다

  ![image](https://github.com/ces0o/Paper-Review/assets/127365253/def22bed-38bd-4d4f-b768-c1c6ead4af97)

  위의 식을 설명하자면 앞에 있는 첫 번째 텀은 normalization 하기 전의 텀이다
  델타가 추가된 텀은 원래 기울기 방향에서 빼주는 역할을 한다
  현재 output과 델타, 즉 두 개의 방향이 일치할 땐 0값이 도출되게 된다
  이 말은 현재 가고 있는 방향 외에도 좀 더 다양한 방향을 보게해준다는 것을 뜻한다
  기울기가 같아지면 기울기가 작아지니까 (점점 0으로 수렴) 기울기가 계속 다른 방향으로 나아갈 수 있게 panalty를 준다

  ## experiment

  <img width="563" alt="image" src="https://github.com/ces0o/Paper-Review/assets/127365253/c5f80e6f-0183-4005-915c-11c78af10c25">  

  그래프에서 보이다 시피 inception score가 고르게 좋게나오는 것을 확인할 수 있다 (Setting 종류에 상관없이)

  

  
  


  


  


  

  










  




  
  






  

  


