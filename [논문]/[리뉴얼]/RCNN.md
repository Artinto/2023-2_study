# R - CNN : Rich feature hierarchies for accurate object detection and semantic segmentation Tech report
* 딥러닝을 활용한 object detection의 최초의 논문.

## What is Vision?
- 비전의 주요 Task
    1. Classification
    2. Object Detection
    3. Image Segmentation

[이미지]  
[이미지 출처](https://velog.io/@boom109/The-evolution-of-object-detection-and-Summary-Object-detection의-발전사)  
* Classification: 이미지에서 객체의 범주(Category)를 식별.  흔히 ImageNet Large Scale Visual Recognition Challenge에 따라 발전됨
* Object detection : 객체를 Classification할 뿐만 아니라 객체가 존재하는 공간(Bounding Box)까지 정의.
* Segmentation : 이미지를 의미 있는 여러 영역으로 분할하는 과정 
    [이미지]  
    [이미지 출처](https://www.jeremyjordan.me/semantic-segmentation/)  
    - 이미지의 pixel들을 어떠한 객체에 속하는지 결정.
    - RGB나 흑백 이미지를 입력으로 넣으면 Segmentation map이 나오게 됨.
    [이미지]  
    [이미지 출처](https://www.jeremyjordan.me/semantic-segmentation/)  
    - Segmenation의 종류
    [이미지]  
    [이미지 출처](https://arxiv.org/pdf/1801.00868.pdf)  
        - Semantic Segmetation
            - 의미론적인 분할로 instance를 구분, 같은 instance면 구분하지 않음.
        - Instance Segmentation
            - 객체적인 분할로 이미지 객체를 구분해 분할(일종의 Semantic + Object detection)
        - Panoptic Segmentation(2018)
            - 총괄적인 분할로 객체의 class와 instance를 구분하여 일종의 Semantic과 instance segmentation을 합쳐진 방식. 
            - labeling이 [Class][instance id]로 labeling이 되어 있음.
            - [논문 링크](https://arxiv.org/abs/1801.00868)

## History of Object Detection
[이미지]  
[이미지 출처](https://www.researchgate.net/figure/Milestones-of-object-detection-and-recognition-including-feature-representations-Csurka_fig7_336934637)  
- object dectecion은 David G lowe의 ImageNet Classification with Deep Convolutional Neural Networks(1999년)([논문링크](https://www.cs.ubc.ca/~lowe/papers/iccv99.pdf))을 시작으로 Vision 분야의 가장 중요한 한 축으로 연구.
- 파란색 영역이 Deep learning을 사용하기 전 Traditional  Detection방법

### 주목해봐야할 점.
* ImageNet
* PASCAL VOC
* Selective Search

#### ImageNet(2006)
- 이미지의 Classification을 위한 데이터 셋으로 딥러닝 발전에 많은 기여를 한 데이터 셋.
- 해당 데이터셋을 이용한 ImageNet Large Scale Visual Recognition Challenge 대회(2010~2017)가 열려서 다양한 Convolution Neural Network가 등장함(AlexNet, ResNet)
- 대회에는 
- 2023년 기준으로 약 1,420만 개의 이미지와 20,000개 이상의 카테고리를 제공

####  - PASCAL VOC(2005)
- object detection을 위한 데이터 셋으로 해당 이미지가 어떠한 Class(ex. 사람, 개, 강아지 등)에 속하여 있는지 어떠한 영역에 존재하는지(bounding Box)에 대한 정보가 제공됨

- 불러오기 예시
```python
import tensorflow_datasets as tfds
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# PASCAL VOC 데이터셋 다운로드
dataset, info = tfds.load('voc/2007', split='train', with_info=True)

# 샘플 가져오기.
examples = dataset.take(3)

# 시각화
fig = plt.figure(figsize=(10, 10))
for i, example in enumerate(examples):
    ax = fig.add_subplot(2, 3, i+1)
    ax.imshow(example['image'].numpy())
    
    # 각 객체에 대한 바운딩 박스와 Class 표시.
    for bbox, label in zip(example['objects']['bbox'], example['objects']['label']):
        ymin, xmin, ymax, xmax = bbox.numpy()
        rect = patches.Rectangle((xmin*example['image'].shape[1], ymin*example['image'].shape[0]), 
                                    (xmax-xmin)*example['image'].shape[1], 
                                    (ymax-ymin)*example['image'].shape[0], 
                                    linewidth=1, edgecolor='r', facecolor='none')
        ax.add_patch(rect)
        ax.text(xmin*example['image'].shape[1], ymin*example['image'].shape[0], 
                info.features['objects']['label'].int2str(label.numpy()), 
                bbox=dict(facecolor='white', alpha=0.5))
    
    ax.set_title('Image {}'.format(i+1))
    ax.axis('off')
plt.show()
```

- 결과
[이미지]

#### Selective Search(2011)
- Traditional Detection(~2012)은 주로 Sliding Window 방법을 사용.  
![image](https://blog.kakaocdn.net/dn/y22Bw/btraRwpfDFY/PFPukvEnEfAOJiRFcl12H1/img.gif)  

- 위의 초록색으로 된 상자가 window(창문)로 크기가 다른 여러개의 window들을 각각 sliding 시킴.
- 다른 방법으로 input 이미지를 다양하게 scale 시키고 고정된 window를 사용하는 방법도 존재.
- object가 없는 영역도 무조건 sliding 되야하며, 여러 형태의 window를 사용해야 하므로, 수행 시간이 오래 걸리고 검출 성능이 상대적으로 낮음.
- 이러한 sliding window의 문제를 해결하기 위해 새로운 object detection 방식인 Selective search 사용.

* Process(진행과정)  
[이미지]  
[이미지 출처](https://blog.naver.com/laonple/220925179894)  
1. Input 이미지에 initial segmentation 진행  
- Efficient Graph-Based Image Segmentation
    - Felzenszwalb(펠젠숼브)가 2004년 논문 발표
    - 사람이 인지하는 방식의 segmentaiton을 위해 graph 사용 → **G(V, E)**
    - **G(V, E)**
        - V(virtex)는 node를 나타내는데, 픽셀이 node를 의미
        - E(edge)는 간선으로 픽셀과 픽셀의 관계를 나타내며 가중치 $w(v_i, v_j)$로 표현  
    [이미지]  
[이미지]  
[이미지 출처](https://vcansimplify.wordpress.com/2014/05/16/graph-based-image-segmentation/)  
    - 가중치는 픽셀간의 유사도가 떨어질수록 큰 값을 갖게 되며, 결과적으로 w값이 커지게 되면 영역의 분리가 일어남.  
    [이미지]  
    [이미지 출처](http://www.huppelen.nl/publications/selectiveSearchDraft.pdf)  
    - 위 그림과 같이 영역 C1과 C2가 있는 경우, 영역을 분리할지, 통합할지는 다음 수식을 이용.  

    [이미지]    
    [이미지 출처](http://www.huppelen.nl/publications/selectiveSearchDraft.pdf)  
    - Dif(C1, C2): 두 개의 그룹을 연결하는 최소 가중치
    - Mint(C1, C2)는 각각의 C1, C2 그룹 내 최대 가중치 2개 중에서 작은 것을 선택한 것.
    - 그룹 간의 차가 그룹 내의 차보다 큰 경우는 별개의 그룹으로 그대로 놔두고, 그렇지 않은 경우에는 두 그룹을 병합하는 방식.

2. 반복적으로 작은 영역을 큰 영역으로 결합(Hierarchical Grouping)  
[이미지]
[이미지 출처](http://www.huppelen.nl/publications/selectiveSearchDraft.pdf)
- R : initial segmentation을 통해 결정된 초기 n개의 후보 영역.
- 영역들 사이의 유사도 집합
- 과정
    - color, texture, size, fill에 대해 유사도를 고려해 각 영역간 유사도를 구함.
        - Bounding Box 간의
    - 유사도가 가장 높은 $r_i$와 $r_j$ 영역을 합쳐 새로운 영역 $r_t$생성.
    - $r_i$와 $r_j$ 영역과 관련된 유사도 삭제.
    - $r_t$와 나머지 영역의 유사도를 계산해 유사도 집합 $S_t$생성하고 기존 $S, R$에 더함.
    
3. 2번 과정을 여러번 반복하여 최종 후보 영역 도출.  
[이미지]
[출처](http://www.huppelen.nl/publications/selectiveSearchDraft.pdf)

## RCNN - Introduce
- Alexnet(2012) 이후에 Object Detection에서도 Deep Learning을 활용하기 시작.
- R-CNN이 딥러닝을 사용한 최초의 방법. 특히 CNN과 결합된.
- R-CNN  : Regions with Convolutional Neuron Networks의 약자. 영역을 설정하고 CNN을 활용해 object detection을 수행하는 신경망.
- 특징
    1. **고용량 합성곱 신경망(CNN)을 하향식 지역 제안(bottom-up region proposals)를 적용하여 객체를 지역화하고 세분화.**
    2. **레이블이 지정된 훈련 데이터가 부족할 때, 보조 작업을 위한 지도 학습 사전 훈련을 시행한 후 도메인 특정 정교화(fine-tuning)를 진행하면 성능이 크게 향상된다는 점**
    

## RCNN - Process  
[이미지]
[이미지 출처](https://arxiv.org/pdf/1311.2524.pdf)

1. 데이터 입력.
2. 2000개의 bottom-up region proposals을 추출
    1. Region Proposal
        - regional proposal : object의 위치를 찾는 localization문제로 R-CNN에서는 Selective Search 사용.

    2. Warp
        - CNN 네트워크의 입력 사이즈에 맞게 Region Proposal의 크기를 wrap(조절)
        - R-CNN에서 CNN으로 alexnet을 사용하기 때문에 227x227 로 맞춰줌.  
        [이미지]  
        [이미지 출처](https://arxiv.org/pdf/1311.2524.pdf)  

        * 1번째 열 : padding = 0, 2번째 열 : padding = 16인 경우를 뜻함
        * (A)행 : Selective Search에서 추출된 Region Proposal.
        * (B)행 : 후보 영역에 원래의 원래의 원본을 덧댐.
        * (C)행 : 후보 영역에 원래의 원본을 덧댐
        * (D)행 : 후보 영역을 정해진 규격만큼 확장
        - (B), (C) 행에서 보이는 회색 빈칸은 CNN 모델에 들어가기 전, 이미지 평균으로 대체됨.
        * 위 논문에서는 경험적으로 16 padding이 있는 채로 확장시키는 것이 더 좋은 성과를 냈다고 함.
        
3. 제안된 영역들을 CNN에 넣음.
-  사전작업
    ![이미지](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2F2ciLD%2FbtqOjmN2tnS%2FDmKE8bDtwoVyPTbKO4kStk%2Fimg.png)
    [이미지 출처](https://herbwood.tistory.com/5)
    - 2000장의 region proposals와 ground-truth box의 lou(Intersection of Union)을 비교하여 lou가 0.5 보다 큰 경우 positive samples, 0.5보다 작은 경우 negative samples로 나눔.
        - lou
            - Intersection over Union의 약자로, 아래의 두 가지가 얼마나 일치하는지 측정하기 위한 평가 지표로 사용됨.
                
                ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/6c785225-d9ac-4a37-aca1-8bd74e4fef1d/fb3a2fff-a0f6-49a5-aabe-e4b6ecb4de0c/Untitled.png)
                
                [이미지 출처](https://wjs7347.tistory.com/10)
                
                - Area of Union : Region proposal과 ground-truth box의 합집합.
                - Area of Overlap  : Region proposal과 ground-truth box의 교집합.
                
                ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/6c785225-d9ac-4a37-aca1-8bd74e4fef1d/2ee1852a-ebf6-468d-9f51-526c41066c76/Untitled.png)
                
                [이미지 출처] https://wjs7347.tistory.com/10
                
                * 위의 예시처럼 겹치는 영역이 클수록 높은 값을 가짐
                
        - 왜 IoU가 0.5 이상인 애들만 사용했는지
            - 실제로 정답 데이터와 30배 이상의 데이터를 학습 데이터를 얻더 overfitting을 방지할 수 있다고 생각했음.
        - Positive sample은 객체가 포함되어 있는 sample을 의미, negative sample은 객체가 포함되지 않은 배경 sample을 의미
        - 이렇게 나눈 후 positive sample 32개 + negative sample 96개 = 128(1:3)개의 이미지로 이루어진 하나의 미니 배치 만듬.
        - 실제로 positive sample은 배경에 비해 매우 드물었기 때문에 positive sample에 bias되어 결과 추론.
        
- **Fine tuning pre-trained AlexNet**
![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/6c785225-d9ac-4a37-aca1-8bd74e4fef1d/8c081f00-0eb1-404a-a689-b24ec5939add/Untitled.png)
- 당시 CNN 학습시 PASCAL VOC의 데이터가 ImageNet에 비해 적어, 2012년에 발표된 AlexNet을 ImageNet에 데이터를 이용해 Pre-training 시킴.
- 그 후 PASCAL VOC의 데이터를 이용해 Fine-tuning.
    - 이때 AlexNet의 output은 ImageNet에 맞춘 1000이 아니라 예측하려는 객체 수 N에 1일 더한  N+1이 되야한다. (배경 추가)
    - R-CNN에서는 PASCAL VOC의 객체가 20개로  21개로 학습.
- 결과적으로 2000개의 Region proposals을 넣어 CNN의 2000x4096(Alexnet의 softmax를 통과하기 전까지)
- 파라미터 갱신에 는 SGD(lr=0.001)를 사용.

4. 선형 SVM(support vector machine)을 이용해 클래스별로 각 지역 분류.
- SVM
    - 분류를 하기 위한 머신러닝 알고리즘으로, 데이터를 가장 잘 구분할 수 있는 경계선(Hyper plane)을 찾는 것이 목표.
    - 여기서 Support vector는 경계선에서 가장 가까운 데이터로 **경계선과 거리가 최대가 되는 경계선을 찾는 것이 Support vector machine의 목표이다**.

    [이미지 출처](https://ropiens.tistory.com/73)

    [이미지출처]([https://velog.io/@hyesoup/서포트-벡터-머신Support-Vector-Macine-SVM](https://velog.io/@hyesoup/%EC%84%9C%ED%8F%AC%ED%8A%B8-%EB%B2%A1%ED%84%B0-%EB%A8%B8%EC%8B%A0Support-Vector-Macine-SVM))
        - 위 그림 중에서 F가 가장 좋은 경계선. (각 margin이 비슷하면서 Margin의 합이 최대)
    - 학습.
        - $h(x)  = W*x+b$
        - $X_s$는 동일한 거리에 있는 점.
        - KKT condition과 라그랑주의 승수법으로 인해서 수식. 다음과 같이 정리됨.
            ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/6c785225-d9ac-4a37-aca1-8bd74e4fef1d/a5bd88a1-6978-491c-ae13-95a4a236c600/Untitled.png)
            
        - 저 L(u)를 최대화하는 것이 목표.
    - 하지만, 위의 과정은 이제 Linear한 경우에만 Seperate가 가능.
        - R-CNN은 Linear SVM을 사용함.
        
- Kernel with SVM
    - Kernel Trick : 기존의 데이터를 높은 차원에서 확인하여 linear하게 separable할 수 있도록 하는 기법.
        ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/6c785225-d9ac-4a37-aca1-8bd74e4fef1d/e2c7e0bc-184a-4c96-a6a9-5744d932c223/Untitled.png)
        
    - 2차원의 데이터를 kernel fuction을 사용해서 3차원으로 확인하여 svm을 적용.
    - Trick?
        - Trick : 속임수
        - Mapping Function : 저차원을 고차원으로 바꿔주는 함수.
            
            ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/6c785225-d9ac-4a37-aca1-8bd74e4fef1d/39bacb3c-0458-459e-9863-1cf83de41875/Untitled.png)
            
        - [이미치출처](https://sanghyu.tistory.com/14)
        - But, 차원을 높이면 계산량이 증가한다는 문제가 발생.
        - 예시
            - 2차원을 6차원으로 높이기
            - $x축 : (X_1, X_2)→ (1, \sqrt{2}X_1, \sqrt{2}X_2, \sqrt{2}X_1X_2, X_1^2,X_2^2) =h(x) $
            - $y축 : (Y_1, Y_2)→ (1, \sqrt{2}Y_1, \sqrt{2}Y_2, \sqrt{2}Y_1Y_2, Y_1^2,Y_2^2) =h(y) $
            - 위 두 식의 내적 결과 : $(1+X^TY)^2 = (1+X_1Y_1 + X_2Y_2)^2 = K(X*Y)$
            - 2차원 데이터의 내적의 제곱이 일종의 6차원의 내적과 동일
            - 즉, 낮은 차원에서 높은 차원으로 변환 후 최적의 값을 찾는것과 동일해짐.
            
            ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/6c785225-d9ac-4a37-aca1-8bd74e4fef1d/9bb1458b-a81c-4910-948e-a51c7b6d502f/Untitled.png)
            
            - 변경된 식.
            - 이를 통해서 linear하게 나눠지지 않는 데이터에 대해서도 linear하게 나눌 수 있다.
        - 자세한 내용은 [정한울 교수님의 머신러닝 중 SVM강의](https://www.youtube.com/watch?v=uCYeM9y5NLo&list=PLrJcoRcsaj2ub5cWet5ojEwckfEKNvgkG&index=17)
        
- R-CNN in linear SVM
    - Linear SVM은 2개에 대한 Classification만 가능
    - N+1개의 SVM이 필요함.
    - 강아지에 대한 bounding box가 에매하게 걸려있는 경우는?
        - IoU에 대해 0.3이상인 경계박스는 positive로 하니 결과가 가장 좋았다.
        - 원래 0.5로 진행했으나 결과가 좋지 않아 0.3으로 변경.
    - 왜 SoftMax는 사용하지 않았는가?
        - 실제로 초기엔 softmax를 이용하여 클래스를 예측했지만 성능이 떨어짐.
        - 성능이 떨어진 요인으로 AlexNet을 finetune할 때 Selective search로 추론된 bounding box들 중 IoU가 0.5~1인 상대적으로 정확하지 않은 예측들이 Positive sample로 포함되었기 때문이라고 주장.
        - 실제로 적잘한 방식으로 fine-tune한다면 svm과 비슷한 성능을 보일것으로 저자는 주장.

### Improvement of RCNN
* 아래 세가지의 기법을 통해 정확도를 더 끌어올림.

- **Hard negative mining**
- 모델이 예측에 실패한(hard) sample들을 모으는 기법.
- 기본적으로 데이터가 객체(Positive)인 경우보다 배경(negative)이 더 많은 불균형으로 인해 모델이 객체라고 예측했지만, 실제로는 배경인 False positive인 오류 발생.
- 이를 모델에 false positive sample들을 추가하여 재학습 진행.
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/6c785225-d9ac-4a37-aca1-8bd74e4fef1d/35b7f563-d7c6-4ea7-91a0-01ee053ee1cd/Untitled.png)
[이미지링크](https://herbwood.tistory.com/5)

- **Bounding Box Regressor**
- Selective Search의 오류를 줄이기 위해 DPM에서 제안된  bouding box Regressor를 사용.
- 기본적으로 Selective search를 통해 나온 Bounding box의 좌표들을 변환하여 객체의 위치를 조정.
[이미지]
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/6c785225-d9ac-4a37-aca1-8bd74e4fef1d/cc81b637-cc7e-43ed-b8a2-3378d98edde5/Untitled.png)
    
- p : Selective Search에 의해서 예측된 좌표(x,y,w,h)
- g : Selective Search에 의해 나온 bouding box의 좌표를 Bouding box regressor 모델이 변환한 결과.
- t : Bounding box regressor 모델이 학습하고자 하는 목표(target)
- d(P) : Bounding box regressor 모델의 학습 대상
- L : loss function로 sum of squared Error(SSE)
- 이때 변환된 결과는 Scale invariant해야한다.
    - 객체의 크기가 변해도 객체의 기본적인 특성이나 형태가 변하면 안됨.

- **Non maximum Suppression**
- 2000개의 Region proposal을 진행할 경우. 하나의 객체에 많은 bounding box가 겹치게 된다.
    - 탐지 정확도 감소.
- Bounding box 중에 가장 비슷한 위치에 있는 box를 선택 후 나머지 box들 제거.
[이미지]
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/6c785225-d9ac-4a37-aca1-8bd74e4fef1d/396a5dab-30e6-4eca-acf6-0f8a98a9b376/Untitled.png)
    
- 동작 순서
    - confidence score threhold 이하의 box 제거.  → 0.3 제거
    - 남은 box 내림차순으로 정렬 → 0.9, 0.85, 0.81, 0.73, 0.7
    - IoU threshold 설정 → 0.4로 설정.
    - 내림차순된 cofidence score와 나머지 박스 간의  IoU 계산 → 0.85 : 0 , 0.81 : 0.44, 0.73 : 0, 0.7: 0.67
    - IoU threshold보다 크면 box제거
    - 이를 반복 후 남은 박스만 선택. → 0.9, 0.85

- **Total process of R-CNN**
[이미지]
![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/6c785225-d9ac-4a37-aca1-8bd74e4fef1d/3aa32ef6-714a-49dc-9da0-c374b196b14b/Untitled.png)

[관련내용](https://herbwood.tistory.com/5)

### R-CNN의 결과
- AlexNet에 어떠한 점을 사용했는 지에 따른 결과표.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/6c785225-d9ac-4a37-aca1-8bd74e4fef1d/03c951c2-12d8-4dea-aca4-2ae85fab24b6/Untitled.png)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/6c785225-d9ac-4a37-aca1-8bd74e4fef1d/71bfda68-25c4-456a-955b-a1df1bd12618/Untitled.png)

[이미지출처]([https://bkshin.tistory.com/entry/논문-리뷰-R-CNN-톺아보기](https://bkshin.tistory.com/entry/%EB%85%BC%EB%AC%B8-%EB%A6%AC%EB%B7%B0-R-CNN-%ED%86%BA%EC%95%84%EB%B3%B4%EA%B8%B0))

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/6c785225-d9ac-4a37-aca1-8bd74e4fef1d/f93a1afc-6b7f-4b49-a595-3a91201063f6/Untitled.png)

- mAP 란?
    * mean Average Precision의 약자로, object detector의 정확도를 측정하는 유명한 평가지표
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/6c785225-d9ac-4a37-aca1-8bd74e4fef1d/e73e45dd-f499-40e0-984f-5d29278ac539/Untitled.png)
    
    [이미지 링크] [Object Detection의 정의와 Metric mAP(mean Average Precision) (tistory.com)](https://herbwood.tistory.com/2)
    
    - IoU의 임계값
        - Actual Class는 Ground truth box이며, Predicted Class는 모델이 생성한 예측 bounding box입니다. 예측 bounding box의 양성 여부는 IoU 임계값을 기준으로 정함
            - IoU 임계값 > 예측 bounding box의 IoU 값 → False
            - IoU 값 > 예측 bounding box의 IoU 임계값 → True
        - 임계값이 낮을수록 더 많은 bounding box를 생성하기 때문에 Recall 값은 높아지나, Precision 값은 낮아짐. 이처럼 Precision과 Recall은 서로 반비례 관계 성립 → Precision/Recall Trade-off라 불림.
    - Precision (정밀도)
        - 모델이 True라고 예측한 것 중 정답도 True인 것의 비율
        - Precision = TP / (TP+FP)
    - recall (재현율)
        - 실제 정답이 True인 것 중 모델이 True라고 예측한 것의 비율
        - Recall = TP / (TP+FN)
    - AP
        - Average Precision의 약자로 Precision과 recall의 값을 종합해서 알고리즘을 평가하기 위한 것
        - Precision-Recall 그래프의 아래 면적을 의미함
            - Precision-Recall
                
                ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/6c785225-d9ac-4a37-aca1-8bd74e4fef1d/899ef64e-0ee2-4192-a97e-0561348a841a/Untitled.png)
                
                [이미지 링크](https://velog.io/@kwjinwoo/mAP)
                
                * 보통 계산 전에 오른쪽 그래프와 같이 바꾼 후 면적을 구함
                
    - mAP는 정의대로 각각의 클래스에 대한 AP 평균을 의미

### R-CNN의 문제점.
- 2000개의 Region proposals
    - 이미지 한 장당 2000개의 region proposal을 추출하므로 학습 및 추론의 속도가 느리다.
- Wrap
    - 이미지를 강제로 CNN에 input size에 맞춰 증가 시켰기 때문에 계산량이 증가되고, 이미지 변형이나 crop으로 인한 정확도가 감소됨.
- GPU 사용에 적합하지 않음
    - Selective Search와 SVM을 사용하는 것이 GPU에 매우 취약.
- 3가지 모델 사용
    - Finetuend AlexNet, linear SVM, Bounding box regressor로 구조가 복잡하고 학습 과정이 복잡함.

### Object-Detection의 발전.
![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/6c785225-d9ac-4a37-aca1-8bd74e4fef1d/1e5ee1a5-b330-48bc-80c4-53fc7e0234c3/Untitled.png)

- anchor?
    - anchor : 닻(고정된 물체) : 이미지 내의 물체 위치를 예측하기 위한 기준점 또는 참조점을 의미
    - anchor-based :물체(객체)가 특정한 형태를 가질 것이라고 가정하고 object detection을 진행.
        - 이미지를 여러개의 고정된 크기와 비율의 anchor box로 분할.
        - anchor box에 object가 있는지, 어떤 종류인지, bounding box는 어떻게 되는지 예측
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/6c785225-d9ac-4a37-aca1-8bd74e4fef1d/70006964-347e-4cbc-a2e6-b59e7855f776/Untitled.png)
    
    [이미지출처]([https://velog.io/@boom109/The-evolution-of-object-detection-and-Summary-Object-detection의-발전사](https://velog.io/@boom109/The-evolution-of-object-detection-and-Summary-Object-detection%EC%9D%98-%EB%B0%9C%EC%A0%84%EC%82%AC))
    
    - 간단하게 2-stage는 모델을 2개, 1-stage는 모델 1개를 사용하는 방식으로 1개만 사용하는 것이 속도가 빠르지만, 2개를 사용하면 정확도가 올라가게 된다.
        - 문제점.
            - object의 크기와 형태에 따른 적절한 anchor를 선택하는 것이 어려움.
            - anchor 수가 많아질수록 연산량 증가.
    - anchor-free : 물체의 중심점을 찾아내어 물체의 크기와 위치를 예측하는 방식.
        - object에 대한 크기와 비율을 사전에 정의하지 않아 더 자유로운 탐지가 가능함.
        - 문제점.
            - 물체의 중심점을 기준으로 하므로, 물체의 형태가 복잡하거나 중첩된 경우 탐지가 어려움.
            - 학습 방식이 anchor-based에 비해 어려움.(중심점을 제대로 탐지하기 위한 학습 필요)
- Transformer
    - **DETR(DEtection TRansformer)**
        - NLP Transformer를 Object Detection 적용
    - 최신 object dection 논문들(2022~2023)에서 Transformer을 사용한 논문들이 대다수이고, 성능도 매우 뛰어남.
    - **Object Detection on COCO test-dev**