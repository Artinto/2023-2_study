# StyleGAN2
## 순서
- PGGAN
  -  [Progressive Growing of GANs for Improved Quality, Stability, and Variation (2018)](https://arxiv.org/abs/1710.10196)
- StyleGAN
  - [A Style-Based Generator Architecture for Generative Adversarial Networks (2019)](https://arxiv.org/abs/1812.04948)
- StyleGAN2
  - [Analyzing and Improving the Image Quality of StyleGAN (2020)](https://arxiv.org/abs/1912.04958)
- StyleGAN3

## Introduction
- 이전 styleGAN에서 발견된 인위적인 결점 2가지를 해결한 버전
  - common blob-like artifact (water shape artifact)
    - ![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/3817e340-aba9-4282-a29a-8164780ecb25)
    - generator의 구조적 결함 문제
  - phase artifact
    - ![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/1793af3b-6e20-41ec-b3bd-206bb15684e9)
    - glowing training 방식의 문제
### Key Insights
- normalization의 변화
  - actual statistics(실제 통계, ex.AdaIN) 방식에서 estimated statistics (추정 통계)로 수정
- skip connection을 갖고 있는 계층 생성자 (hierarchical generator)를 사용
- 이미지 질 개선을 위해 perceptual path length 개념을 regularization에 도입

## Common blob-like artifacts
- 현상
  1. 생성된 이미지에는 artifacts가 두드러지지 않지만, feature map에서는 잘 확인됨
  2. 거의 모든 이미지가 64x64 feature map부터 생성됨
  3. 물방울 모양이 없는 경우는 대부분 최종 이미지가 제대로 생성되지 않는 경우임
  4. progressive growing 되면서 artifacts가 점점 더 커짐
- 결과
  - 데이터 상의 문제가 아닌 시스템의 구조적인 문제 (이미지가 잘못 생성되거나, 64x64 이전에는 찾아볼 수 없음)
  - normalization 단계를 제거하면, artifacts가 완전히 사라짐
  - discriminator가 artifact를 감지하지만 없애지 못하는 이유는 저자들도 찾지 못함
  
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/7853ced5-4afd-4910-94b3-41084d101482)  
- 원인
  - **AdalN**의 구조적 문제 때문
    1) 각 channel 별로 feature map마다 평균과 분산으로 normalization
    2) statistics data를 input으로 normalization
    - channel 별로 다른 값으로 scaling 되어서 합쳐지면서 범주에 벗어난 값 등장
    - 값이 너무 작거나(검) 값이 너무 큰(흰) 부분 -> local한 부분으로 인한 spike 값
    - 평균과 분산을 사용하기 때문에 각 feature map 사이의 관계를 알지 못함 (범주에 벗어난 값인지 알지 못함)
    - 실제 통계를 기반으로 normalization하기 때문에 이상한 값도 그대로 반영
   
- 우연한 계기로 normalization을 제거하니 artifact가 사라짐 -> normalization과 artifact 사이의 관계 확인 
- 새로운 instance normalization 방법이 필요


![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/c8da9bb4-006b-4ccd-b03f-904909582331) 
 
### Generator architecture revisited

![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/7dd8bd6b-05d7-46cb-9dfb-415938d31975)  

#### 구조
- (b) : 기존 styleGAN
  - mean, std로 normalization, modulation
  - AdaIN modulation으로 style을 입힘
  - style block 안에 noise와 bias 존재
- (c) : 초기의 새로운 styleGAN
  - 시작부분의 input에 nor, bias, noise 제
  - normalization과 modulation에 표준편차(std)만 사용
  - bias와 noise는 style block 밖에서 진행

#### 정리
- 전체적으로 generator에서 필요없는 부분은 제거하고, 안좋은 영향을 줄이는 방향으로 변화
  - mean이 없어도 충분히 원하는 normalization효과와 style modulation을 할 수 있음
  - 초기 input에 normalization과 noise, bias를 넣지 않아도 안전하게 동작
  - normalization을 진행하기 전에 bias와 noise가 들어오기 때문에 bias와 noise의 영향이 작아 많이 반영되지 않음
  - normalization이후 modulation 전에 bias와 noise를 더해주면서 영향력을 키움
  
### Instance normalization revisited
- normalization 효과는 얻지만, artifact는 제거하고 싶음
  - artifact를 제거하기 위해 channel 별로 normalization을 진행하지 않음
  - 값의 증폭을 막는 것을 원함
#### 구조  
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/be0d44f6-6e15-45b4-9d90-fa82192eef72)  
- (c) : 초기의 새로운 styleGAN
  - modulation > convolution > normalization 진행
- (d) : 최종 styleGAN
  - normalization 삭제
  - demodulation 추가
  - ![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/a0edaadb-5624-4e6f-ae70-df65a53e1f26)
    - feature map은 건들이지 않고 weight를 건들여서 artifact 문제 해결
      - feature map들에 강제적인 normalization을 진행하지 않아 channel 간 관계 유지
      - convolution을 통해 weight를 건들여서 값의 증폭 방지

#### 정리
- 예측 통계를 기반으로 normalization 진행
  - normalization을 진행하지만, 강제적이지 않도록 진행  
- feature map을 통한 normalization 제거하여 artifact 문제 해결
  - **modulation** (스타일 정보를 채널에 적용)
    - std로 나누는 과정을 없애면서 normalization 삭제
    - A에서 넘어온 scaling factor를 convolution weight에 곱하여 scaling 진행
      ![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/aae4c7fd-b9a1-4a10-ab3d-83190406da4a)  

  - **demodulation** (안정적인 학습을 위해 magnitude 조절)
    - weight를 L2 normalization 사용하여 정규화 진행
      ![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/3adc9646-ed6a-4bba-a9bb-fa5f3dc8ee13)  

    - 각 출력 feature map인 j가 분산이 1이 될 수 있도록 1/(j의 표준편차)로 스케일링
      ![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/8ef8081a-9b4d-45d7-a381-45ff7bee890b)  
#### 추가 및 결과  
- feature map normalization과 weight normalization이 이론적으로 동일하려면 **통계적 가정** 필요
  - input이 i.i.d random variable이어야 함
  - demodulate는 통계적 가정에 기반한 변환
- 실제로 가정을 만족하긴 어렵지만 어느정도 간접적인 효과를 보임
- artifact도 사라짐
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/a98e0016-0553-4c71-8e4e-8fe26e748b4c)  
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/13cce564-a96d-4d46-a493-c794c65d4f18)


## Phase artifact
- 현상
  1. Phase articacts 발생 ( 특히 눈동자나 치아에서 )
  2. 눈동자나 치아 모양은 잘 생성됨
  3. 자세를 바꾸거나 각도가 달라져도 위치가 고정되어 변하지 않는 문제 발생
- 원인
  - **Progressive growing** 이라는 학습 방식의 문제 때문
    1) 저해상도에서 고해상도 이미지로 발전시켜서 훈련하는 방식
    2) progressive growing 구조는 각 resolution이 독립적
    3) 독립적이지만 점진적인 학습이 눈동자나 치아의 위치를 고정하려는 경향을 강하게 만듦 
    
### Progressive growing revisited
- PGGAN
  - 각 resolution마다 완전히 학습하며 먼저 low-resolution features를 만들고 finer detail을 채우는 방식
- progressive growing 방식을 따르지 않고 **feedforward 네트워크**를 활용해서 high-quality 이미지를 생성할 수 있도록 styleGAN 변형

### Alternative network architectures
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/c6082b71-66d6-4a53-853c-a6c3ef58db55)
- tRGB
  - output tensor에서 channel의 크기를 3으로 바꿔서 사람이 확인할 수 있는 이미지 형태로 바꾸어주는 layer
- fRGB
  - 이미지 형태 3channel tensor로부터 입력을 받게 해주는 layer
- MSG-GAN
  - 동일한 resolution의 G와 D를 skip connection으로 matching
- Input/output skips(skip connection)
  - G의 output을 다 더 해서 D로 전달
- Residual nets(residual connection)
  - G와 D 내부에서만 각각 residual learning 사용
  
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/cb2b2962-4875-455c-8e57-6a2a79f270ed)  
- skip connection과 residual networks의 조합 실험
  - generator에서 skip connection은 유용함
  - discriminator에서 residual은 유용함
  - progressive growing 없이 각각 skip generator, residual discriminator 사용
  - phase artifact 개선 및 FID, PPL 성능 상승 

## Image quality and generator smoothness
- 이전에는 생성모델의 평가지표가 FID 또는 Precision, Recall이었음
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/68a69c4f-78dd-47f7-9228-0dba861b80fd)
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/9a6e0065-7866-4e60-823c-9281d23bcb3c)  
- FID나 Precision, Recall이 같더라도 PPL이 낮으면 더 좋은 질의 이미지가 만들어짐
  - FID : 생성된 영상의 집합과 실제 생성하고자 하는 클래스 데이터 분포의 사이의 거리
  - Precision : 정밀도, 모델이 True라고 분류한 것 중 실제 True 비율
  - Recall : 재현율, 실제 True인 것중 모델이 True라고 예측한 비율
  - PPL(Perceptual Path Length)
    ![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/7056fa98-d700-449d-9e7c-edd810d1ad07)
    - input과 output 사이 잠재 공간의 거리



