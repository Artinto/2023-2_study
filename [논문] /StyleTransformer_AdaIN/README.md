# AdaIN (Adaptive Instance Normalization)
[Arbitrary Style Transfer in Real-time with Adaptive Instance Normalization](https://openaccess.thecvf.com/content_ICCV_2017/papers/Huang_Arbitrary_Style_Transfer_ICCV_2017_paper.pdf)
## Introduce
- 이미지의 style을 변경하는 style transfer의 성능을 개선하기 위해 고안된 기법
- **style transformer**
  - 이미지 스타일을 변환하거나 다른 이미지의 스타일을 적용하는데 사용되는 딥러닝 모델
- 기존의 style transformer
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/b86f1458-45e9-4e15-be40-1a30a3eda4a8)  
  - 초기 framework
    - 느리고 반복적인 초적화 과정을 요구 하기 때문에 현실적으로 적용하기 어려움
    - 여러개의 style을 한번에 전송하지만 속도가 느림
  - FFNN을 적용한 transformer
    - 속도가 빠르지만 1개의 style 전송
- AdalN 방식은 빠른 속도로 추론이 가능하면서 동시에 Arbitrary(그때 그때 새로운 style)하게 적용 가능
- lnstance Normalization 개념을 통해 속도를 세자리수 (약 100배) 이상 개선

## Normalization

### Batch Normalization
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/7a2f42f8-2b67-48b7-958f-fa69712861c2)  
- discriminative 네트워크의 훈련을 가속화할 수 있도록 디자인 되었지만, generative image modeling에도 효과적
- **배치** 단위로 각 채널의 정규화 수행
- 표준편차 계산에서 배치 영역을 기준으로 계산 진행
- 일반적으로 네트워크를 훈련할 때 사용하는 정규화 방식
  - 훈련 데이터의 배치에서 각 층의 활성화 값들을 평균과 분산으로 조정
  - 훈련 과정에서 gradient 소실 문제를 완화하고 학습속도를 빠르게 할 수 있음
- 분류문제를 해결하는 모델에서 효과가 좋으며, 훈련시간이 줄어듦

### Instance Normalization
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/a129dc81-e868-4f93-a7c6-806e7eb43e91)  
- **채널** 단위로 샘플(instance)의 특성을 개별적으로 정규화
- 표준편차 계산 시 배치 영역을 포함하지 않고 계산 진행행
- 이미지의 픽셀이나 특성 맵을 개별적으로 정규화하기 때문에 이미지 스타일을 변경하거나 적용하기 유리

### AdaIN
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/3b6627dd-921d-48dc-a64f-2274f1fe7778)  
- BN, IN과는 달리 정규화 과정에서 사용되는 파라미터가 없는 방식
- 평균과 표준편차를 계산할 때 주어진 스타일 이미지의 스타일 특징에서 평균과 표준편차를 계산
- 콘텐츠 이미지의 특징에 스타일 특징을 계산한 값을 역으로 입혀 스타일 변환
- 스타일을 전이한다고 생각하면 

## Loss funtion
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/77496b53-858e-410f-964b-ef6a0c81a35b)  
### Content Loss(Lc 보라색 화살표)
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/88649815-209e-4859-8006-d314af092c20)  
- content 이미지에서 콘텐츠(내용) 특징을 보존하기 위해 사용
- t(style transfer network)를 디코더에 넣고 다시 인코더에 넣어 차이 비교
- style transformer의 output과 목표 이미지 사이의 픽셀 차이를 측정
- MSE(평균 제곱 오차)를 사용하여 계산

### Style Loss (Ls 빨간색 화살표)
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/39f27682-57ac-445b-9712-cb7739f19ee4)  
- style 이미지의 style 특징을 보존하기 위해 사용
- 기존 이미지 s를 인코더에 넣었을 떄의 평균(파이(s))과 t를 디코더에 넣고 다시 인코더에 넣었을 때 평균(파이(g(t)))을 최소화 시키는 방법으로 loss 구현
- style transformer의 output과 목표 이미지 사이의 스타일 특징 차이를 측정
- Gram Matrix를 사용하여 계산

## Architecture
- 내가 원하는 Contents를 담고 있는 이미지의 feature x 에서, 이미지의 스타일을 빼주고, 내가 입히고 싶은 Style을 더해주는 방식으로 수행
- Encoder
  - 입력 이미지를 인코딩하여 이미지의 콘텐츠 정보를 추출하는 부분
  - 이미지의 주요 특징과 구조를 임베딩
  - 일반적으로 CNN을 사용하여 이미지의 특징 추출
- Decoder
  - 스타일 이미지의 특징을 인코더에서 추출한 콘텐츠 이미지의 내용과 결합하여 새로운 이미지를 생성하는 부분
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/800538c6-b168-455a-8575-e0e74437efd2)  
- VGG-19 Encoder
  - style image와 content image를 넣어 각각 feature embedding 생성
  - 사전에 대규모 데이터셋에서 훈련된 pre-trained 모델사용
  - encoding을 수행하여 콘텐츠 정보를 추출할 뿐(feature을 추출할 뿐), encoder는 학습시키지 않음
  - encoding 과정에서 이미지를 잠재공간(의미론적인 특징이나 표현을 담는 추상적인 공간)으로 변형

- AdaIN
  - AdaIN 내에는 학습이 가능한 파라미터가 없는게 특징
  - 즉 AdaIN은 이미 정의된 수식을 따르며 학습되지 않음
  - feature에 대한 통계를 계산하여 decoder에 입력시켜주는 역할
  - 평균(mean)과 표준편차(std)를 사용하여 컨텐츠 이미지의 특징을 정규화
  
- Decoder
  - AdaIN을 통해서 생성된 feature의 정보를 바탕으로 이미지를 다시 이미지공간(눈으로 볼 수 있는 일반적인 이미지 정보)으로 변환
  - decoder는 이미지 공간으로 변환하는 방법을 학습 (어떻게 스타일 된 이미지를 생성하는가를 학습)
  - 학습을 통한 가중치를 optimization
 
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/3b6627dd-921d-48dc-a64f-2274f1fe7778)  
- ![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/6f7867ec-b127-4655-92e1-1e7ffd321c32)
  - 콘텐츠 이미지에서 콘텐츠 이미지의 스타일을 추출
- ![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/b3aebe35-0de0-413d-9a76-cb26a6f04993)  
  - style 이미지 y의 스타일을 출력 이미지에 적용

- 즉 decoder에서 정규화 방식을 진행할 때 no normalization이 가장 성능이 좋음 (AdaIN)
