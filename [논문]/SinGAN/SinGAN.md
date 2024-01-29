## SinGAN : Learining a Generative Model from a Single Natural Image

![image](https://github.com/ces0o/Paper-Review/assets/127365253/46ff2273-5025-4c8f-a1c9-eb3a556ceb8a)  
﻿Image generation learned from a single training image

﻿이 논문은 하나의 그림으로 있을법한 여러장의 이미지를 생성하는 것을 목표으로 한다
여러장의 input dataset을 사용하는 GAN과 달리 하나의 이미지만을 사용한다는 것이 특징

### Abstract  
﻿SinGAN이란 하나의 자연적인 이미지로부터 학습을 진행하는 모델이다 
이 모델은 내부 분포를 포착할 수 있도록 훈련되어 있고, 이미지 내 패치를 적용한 후 높은 값을 생성할 수 있게 된다

동일한 시작적 내용을 담고 있는 품질, 다양한 샘플 이미지로서 SinGAN은 완전한 convolution GAN의 pyramid를 포함한다.  
상당한 가변성을 가지면서도 훈련 이미지의 global contstruction과 미세한 질감을 유지한다.  

### Introduction  
﻿GAN에 대한 연구가 계속 되고, 학습을 하기 위해 많은 수의 데이터가 필요하는 한계
또한 다양한 class로 구성된 dataset의 distribution을 배우는 것은 학습이 잘 진행되지 않았고, 이러한 문제점이 계속되었기 때문에 다음과 같은 아이디어가 도출

“적은 수의 image만 가지고 GAN을 학습시키면 어떨까?”  

위와 같은 idea를 토대로 SinGAN에 대한 논문이 발표되었다.  

### Method  
﻿SinGAN의 목표는 single training image의 내부 통계치(distribution)을 배울 수 있는 unconditional generative model을 만드는 것이다.  
이를 위해 Image의 배열과 Objecti들의 모양 등의 Global한 특징과 Object의 디테일한 정보, Texture 등 Fine한 특징을 모두 배울 수 있어야 한다.  
이를 위해 Coarse-to-fine하게 image를 생성하는 multi-scale GAN 구조를 사용한다.  

![image](https://github.com/ces0o/Paper-Review/assets/127365253/878ad9c6-a324-49b3-8779-cc3a54acf7f6)  

﻿그림에서 x0은 traing image이고 아래로 한 단계씩 내려갈수록 r배씩 downsampling되는 방식이다.  
각 단계마다 Generator는 noise와 이전 단계에서 생성한 결과 image를 input으로 하여 image를 생성한다.  

이는 앞서 리뷰논문을 진행하였던 Resnet의 모델의 기반으로 학습이 진행된다는 것을 알 수 있다.  
즉 잔여 학습(residual learining)을 이용하여 세밀한 정보를 추가하는 방식을 사용한다.  
그 단계의 Discriminator는 downsampling된 Generator와 생성된 image를 구분하도록 학습이 된다.  
예외와 제일 첫 단계(맨 밑)에서는 noise만을 이용하여 image를 생성한다.    

downsampling된 generator를 생성하도록 학습을 진행시키기 때문에 coarse한 특징에 집중을 하여 생성을 하게 되고, 위로 갈수록 fine한 영역에 집중하여 생성을 하게 된다.  

정리하자면 Generator는 위쪽의 G로 올라가면서 세밀한(fine) 정보를 추가하고 Discriminator는 패치단위로 판별을 진행한다.  

![image](https://github.com/ces0o/Paper-Review/assets/127365253/ab8ae1e3-2047-4c91-b9f2-250bd176680f)  

﻿학습을 진행하면서 Generator가 training image 자체를 외울 수 있기 때문에 적은 capacity를 갖도록 설계를 하였다.
구조는 3x3 Conv-BatchNorm-LeakyReLU를 5번 반복한 간단한 Fully-Convolution 구조이고 제일 coarse한 Generator는 32개의 kernerl을 사용한다.
4개의 scale이 오를 때마다 kernel 개수를 2배로 해준다
각각의 생성자는 다음의 연산을 수행한다.  

![image](https://github.com/ces0o/Paper-Review/assets/127365253/844ffce1-1ee4-414f-8afa-58480895e07e)  

﻿위의 식의 첫번째 term에서 완전히 이전 단계의 이미지 자체가 더해져있는 것을 확인할 수 있다.
이러한 방식을 사용하게 되면 앞에서 연산한 결과를 그대로 사용하고 추가로 학습해야할 잔여정보만을 학습하도록 만들기 때문에 network의 학습 난이도가 낮고 그로인해 더욱더 깊은 layer를 학습할 수 있다는 장점을 가지고 있다.  

Singan의 목적 함수  

![image](https://github.com/ces0o/Paper-Review/assets/127365253/4f29ab07-5395-4416-8d89-19fdc00f8fd7)  

﻿각 GAN의 모델은 다음의 목적 함수를 이용해 학습을 진행한다.
1. Adversarial loss : 실제 이미지내 피치와 가짜이미지내 패치의 분포가 같도록 학습
2. Reconstruction loss : 실제 이미지를 정확히 생성할 수 있도록 학습

![image](https://github.com/ces0o/Paper-Review/assets/127365253/eae0a32d-1233-4793-aa9e-0a7f9c3b7e51)

노이즈 값으로 0을 넣었을 때 실제 이미지와 동일한 이미지를 생성하게 설정

### RESULT  
﻿학습된 SinGAN의 생성자를 사용할 땐 원하는 scale부터 설정할 수 있다.
G(N)부터 사용한다면 다양한 이미지를 만들 수 있으나 원본 이미지와 매우 다른 형태의 이미지가 생성될 수 있다.
X(N)에 다운샘플된 실제 이미지를 넣고 G(N-1)부터 이용한다면 원본 이미지의 가장 coarse한 내용은 유지한 상태로 세밀한 정볼르 다양하게 변경해 볼 수 있다.  

![image](https://github.com/ces0o/Paper-Review/assets/127365253/a3cb6e0d-dc79-4cda-aeec-9d1fde982b6d)  

![image](https://github.com/ces0o/Paper-Review/assets/127365253/46ebb4ec-9695-48bd-88c7-781893621cbc)  

﻿위의 결과처럼 첫 번째 스케일(n)으로 설정하면 다양성이 높아지지만 그럴싸하지 않은 이미지가 나올 수 있다 (Confusion이 50%에 가까워질수록 사람이 구분하는 것에 혼동을 느낀다는 것을 의미)  

![image](https://github.com/ces0o/Paper-Review/assets/127365253/88d333f0-9812-4e42-9570-685835ef8aaa)

﻿이처럼 Generator가 Fully-Convolution의 구조이기 때문에 임의의 해상도를 갖는 이미지를 생성할 수 있다.  
﻿입력, 출력 Size를 조절할 수 있기 때문에 이와같은 결과를 얻을 수 있다.

![image](https://github.com/ces0o/Paper-Review/assets/127365253/49b6814f-3218-4974-b3c0-ec63d1c18ca9)  

SRGAN과 같이 외부 데이터 셋으로 학습하는 방법과 비교해도 좋은 성능을 보인다  

### Applications  

![image](https://github.com/ces0o/Paper-Review/assets/127365253/7a41896e-5631-4585-a9e8-0d55ae57712b)  

﻿Coarse level중 (N-1 혹은 N-2)하나의 입력으로 클립아트를 넣어 그림을 이미지로 변환한다.
클립아트의 global structure은 유지한 상태로 세밀한 텍스터가 추가되는 것을 알 수 있다.  

![image](https://github.com/ces0o/Paper-Review/assets/127365253/e4695c2b-e64a-47a6-8ee6-bbe8e15b4f82)  

﻿image에서 일부 영역들을 복사+붙여넣기 하여 편집을 하였을 때 편집된 image를 주변에 자연스럽게 어우러지도록 만들어주는 Editing 예시이다.
아래 결과 그림 처럼 포토샵에 들어있는 기능인 Content Aware Move기능보다 더 자연스로운 결과를 보여주는 것을 확인할 수 있다.
