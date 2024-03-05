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