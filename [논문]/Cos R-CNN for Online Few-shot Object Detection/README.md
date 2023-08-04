# Cos R-CNN for Online Few-shot Object Detection

## Abstract
* Cos R-CNN, R-CNN formulation is designed for online few-shot object detection
* Cos R-CNN frames detection as a learning-to-compare task
* The cosine-based classification head allows for dynamic adaptation of classification parameters to the exemplar embedding
* The cosine-based encourages the clustering of similar classes in embedding space without the need for manual tuning of distance-metric hyper parameters
* Use a simple formula

## Introduction
* 예제를 사용하여 기본 탐지기를 훈련한 다음 데이터가 부족한 새로운 클래스 예제를 사용하여 기본 탐지기를 미세 조정하는 2단계 훈련 파이프라인에 의존하고 있음
* Fig. 1과 같이 Few-shot learning은 미세 조정 없이도 보이지 않는 클래스를 감지할 수 있는 모델을 훈련 할 수 있음
* Cos R-CNN은 R-CNN의 일반적인 구조를 따르지만, 알려진 레이블의 예시와 유사한 객체의 위치를 생성하도록 학습
* 최근 Few-shot learning clasification의 접근 방식은 코사인 거리를 사용하는데 있어 모든 클래스의 로직을 동일한 범위로 확장하기 때문에 코사인 거리를 유사성 측정값으로 사용
* 코사인 기반 메트릭 학습은 각 반복에서 많은 양의 데이터를 표시할 때 이점을 얻을 수 있음
* R-CNN 기반 프레임워크는 작은 배치크기에서도 훈련 중에 큰 메모리 공간을 차지하기 때문에 일반적으로 이러한 공간을 차지하기 때문에 일반적으로 이러한 이점을 얻기가 어려움
* 이 문제를 해결하기 위해 훨씬더 큰 규모의 예시 코퍼를 비교하여 학습 프로세스를 개선할 수 있는 MoCo의 변형인 Su-MoCo도 도입
<a href='https://ifh.cc/v-fqRYKJ' target='_blank'><img src='https://ifh.cc/g/fqRYKJ.jpg' border='0'></a>
#### Fig. 1

## Related Work

### A. Few-shot Classification
* 최근 등장한 개념은 메타 학습으로, 모델이 몇개의 짧은 작업으로 구성된 '에피소드'를 반복하여 학습하도록 설정하는 방식
* 단발성 작업의 분포를 학습함으로써 향후 발생할 수 있는 모든 단발성 작업으로 일반화하는 것을 목표
* Prototypical Networks와 Relation Networks 전략은 Few-shot Learning에서 유용하게 사용될 수 있는 전략
  > Protypical Networks : 쿼리 임베딩과 메타학습된 클래스 프로토타입 간의 유클리드 거리를 비교하여 가장 가까운 쌍을 매칭
  
  > Relation Networks : Prototypical Networks를 확장하여 유사도 측정 방법을 학습 가능한 관계 모듈을 도입하여 수행

### B. Few-shot Object Detection
* 대부분의 방법은 풍부한 기본 클래스에 대해 먼저 base detector를 훈련한 다음 부족한 새로운 클래스에 대해 미세 조정하는 2-stage training pipeline을 제안
* 최근 FSDet에서 가중치를 동결하고 R-CNN 검출기의 마지막 박스 헤드 레이어만 미세 조정하는 간단한 전략이 많은 최신 Few-shot Object detection 방법에 비해 우수
* 이와 관련된 모델로는 Fewshot-YOLOv2, Meta-RCNN, MetaDet, RepMet이 존재

## cos R-CNN
<a href='https://ifh.cc/v-9tgJzj' target='_blank'><img src='https://ifh.cc/g/9tgJzj.jpg' border='0'></a>
#### Fig. 2 (cos R-CNN architecture)
* 일반화를 위해 중요한 것은 동일한 객체 유형의 다양한 예제를 통해 학습한다는 점입니다.
* 신중한 정규화 없이 새로운 클래스를 탐지하기 위해 학습을 시도하면 소수의 특정 예제에 과적합할 가능성이 높기 때문에 이 공식은 소수 샷 탐지에는 적합하지 않음

### A. Examplar Embedding Pathway
* 구조는 Faster R-CNN과 거의 유사
  > 첫 번째 단계는 후보 오브젝트와 그 binding box를 제안하는 지역 제안 네트워크(RPN)라는 하위 네트워크
  
  > 두 번째 단계를 네트워크 헤드로, 후보 객체를 분류하고 경계 상자를 구체화하는 것을 목표로 하는 작은 하위 네트워크
  
  > 후보 객체를 분류하고 boundary box를 구체화하는 것을 목표
  
* Back born을 공유하면 별도의 back born을 사용할 때와 같이 네트워크 크기/메모리 소비를 크게 늘리지 않고 예시 기능을 생성

### B. Cosine Comparator Head
* Cosine similarity/distance is defined as

$$
C<sub>i</sub> = cos(W<sub>i</sub>,x) = \frac{W<sub>i</sub>}{|W<sub>i</sub>|} - \frac{x}{|x|}
$$
 
  > 여기서 i = 1,2,...,m은 m 방식 분류 작업에서 i 번째 클래스를 나타냅니다. W<sub>i</sub>는 Cos R- CNN 백본의 예시 경로를 통해 예시 인스턴스로부터 동적으로 계산되며, X는 임베디드 이미지 피쳐

  > 쿼리와 예제의 교를 통해 분류 수행

  > 모델은 새로운 클래스 예제와 비교하여 새로운 클래스 쉽게 적용

  > L2 정규화 항은 기본/신규 클래스 모두 분류 가중치가 [-1, 1]으로 binding되어 미세조정 없이 분류 가능

* 실제로는 상자 클래스 헤드의 완전히 연결된 분류 레이어를 쿼리 및 예제에서 스케일 코사인 유사도를 계산하는 코사인 비교 레이어로 대체

$$
C<sup>'</sup><sub>i</sub> = λ \cdot cos(W<sub>i</sub>,x) + β
$$

  > λ, β는 학습 가능한 스칼라 스케일과 바이어스 매개변수

  > 코사인 공식의 장점을 그대로 유지하면서 도메인을 [-∞, ∞]로 확장하여 클래스 로그 분포의 피크성을 제어하는 방법을 학습

* Background logits을 예시에서 계산된 logits과 연결 후 softmax화하여 교차 엔트로피 손실 목표에 전달하고, 이를 다시 backpropagate하여 모델을 훈련

* 전체적을로, m-way, 1-shot 작업에서 클래스 i의 후행에 대한 정의를 다음과 같이 증명

$$
p(y=i|x) = \frac{exp(c'<sub>i</sub>)}{exp(\phi<sub>{bg}</sub>(x)) + \sum_{j}^m exp(c'_j)}
$$

 > Few-shot Inference : Cos R-CNN을 m-방향, n-샷 탐지 작업으로 확장하는 방법 중 하나는 다음과 같음

 > 각 m 클래스에 대해 n개의 예시를 제공. 그런 다음 추론은 n - m-방향, 1샷 검출로 이어짐

  > 그러나 소프트맥스를 n - m개의 예시 전체에 걸쳐 코사인 유사도 로그에 적용한 후, 각 클래스에 대한 탐지 점수는 동일한 클래스에 속하는 n개의 예시에서 얻은 점수의 합으로 계산

* m-way, n-shot task에서 클래스 i의 후행은 다음과 같이 주어짐

$$
p(y=i|x) = \frac{\sum_{k}^n exp(c'<sub>j</sub>)}{exp(\phi<sub>{bg}</sub>(x)) + \sum_{j}^n \sum_{k}^n exmp(c'<sub>jk</sub>)}
$$

* comparator-based classification의 경우 테스트에 사용된 것과 동일한 수의 샷(n)으로 훈련하는 것이 유리함

### C. Supervised Momentum Contrast(Su-MoCo)

* Cos R-CNN도 대조적 방식으로 학습되기 때문에, supervised 방식으로 학습되더라도 이점을 얻을 수 있다.
* 그러나 R-CNN architectures는 Rol 샘플링 휴리스틱으로 인해 훨씬 더 많은 양의 GPU 메모리를 사용하기 때문에 단순히 batch 크기를 늘리는 것은 간단하지 않음
  
* Memory Bank
  > 한 가지 해결 방법은 계산 그래프에서 이러한 예시를 분리한 후 Memory Bank에서 이전 반복의 예시 특징을 직렬화하는 것
  
  > 그 후 현재 훈련 반복에서 이 뱅크에서 무작위로 특징을 샘플링하여 현재 batch에 추가 인스턴스를 추가
  
  > 직렬화된 exemplars는 메모리를 거의 소모하지 않아 효과적으로 'batch size'를 늘릴 수 있음

  > 단점으로는 무작위로 샘플링된 예시가 훈련 중 네트워크 진화의 매우 다른 단계에서 생성되었을 수 있으므로 일관성이 없을 수 있음

* MoCo
  > Memory Bank에서 샘플링하기 위해 FIFO를 채택하고 메인 네트워크의 복제본을 사용하여 메인 네트워크보다 느리게 업데이트되는 exemplar featrues을 생성함을써 Memory bank 문제를 해결
  
  > 샘플링 된 예시가 가능한 한 일관성을 유지할 수 있음
  
* Su-MoCo도 MoCo와 마찬가지로 예시 경로에 대해 느리게 진화하는 중복 모델을 활용하고 모멘텀 규칙에 따라 가중치를 업데이트
* 즉, 동일한 업데이트 규칙을 사용하여 중복 모델 가중치를 계산

$$\theta_k \leftarrow \alpha\theta_k + (1-\alpha)\theta_q$$

  > 여기서 θq는 훈련 중인 최신 메인 네트워크의 가중치이고 α는 모멘텀 값

* InfoNCE와 같이 하나의 unsupervised 손실을 사용하는 MoCo와 달리 Su-MoCo의 지도 supervised 손실은 다른 대기열 샘플의 으의 로그 확률 평균

$$
L=-\frac{\sum_{q}^l (log p<sub>l</sub>)}{q}
$$

  > pl은 특정 대기열 l에 대해 계산된 식의 후행이고 q대기열 크기

* Su-MoCo를 사용하면 한 번의 반복에 비교되는 예제의 양을 상당히 늘릴 수 있어 Cos R-CNN 성능에 도움이 됨

## Experiments

* 5-way ImageNet과 20-way Pascal VOC, 이 두 가지 테스트를 통해 에피소드 방식과 비에피소드 방식 모두에서 벤치마킹

### A. Few-shot ImageNet

* 100개의 기본 클래스 예제에 대한 훈련 후, 모델은 보이지 않는 214개의 새로운 클래스에 대해 5-way, n-shot few-shot 작업의 500개 에피소드를 평가하여 테스트

#### 1) Model :

* ResNet50-FPN back born이 있는 더 빠른 R-CNN을 기반으로 한 검출 모델을 사용

#### 2) Traning :

* 모멘텀 0.9, 가중치 감소 10^-4을 사용하여 240,000회 반복에 걸쳐 SGD를 사용하여 모델을 훈련
* 각 GPU의 각 반복은 1개의 쿠리 이미지와 5개의 예시 인스턴스로 구성된 에피소드로 구성
* 효과적인 예시 배치 크기를 확장하기 위해 Su-MoCo 사용하지 않음

#### 3) Inference :

* 훈련 schedule이 끝날 때 모델을 사용하여 RepMet에서 사용한 것과 동일한 500개의 에피소드를 사용하여 새로운 하위 집합을 평가하고, 정확한 에피소드가 제공되지 않으므로 기본 하위 집합에 대해 자체 에피소드를 샘플링

<a href='https://ifh.cc/v-nraPSz' target='_blank'><img src='https://ifh.cc/g/nraPSz.png' border='0'></a>
#### TABLE 1

> AP50 scores on 5-way ImageNet LOC test propsed in repMet

> 새로운 클래스에 대한 fine-tuning 없이도 1-shot, 5-shot, 10-shot에서 향상된 결과를 얻음

#### 4) Results :

* 기본 클래스와 신규 클래스 탐지 모두에서 최첨단 RepMet보다 성능이 뛰어남
* 각 클래스의 여러 예제를 조합하여 Cos R-CNN이 탐지 성능을 향상시킬 수 이씀을 보여줌
* 한 가지 중요한 점은 Cos R-CNN은 원샷 시나리오에서만 학습되었으며, 온라인에서 소수샷 감지가 수행된다는 점

### B. Few-shot VOC

* PAS-CAL VOC 객체 감지 데이터 세트를 기반으로 하며 각각 15개의 기본 클래스와 5개의 신규 클래스로 구성된 3개의 서로 다른 분할로 구성
* 이 테스트는 다양한 클래스 조합의 여러 에피소드를 구성할 수 있는 few-shot ImageNet과 달리 에피소드 단위가 아니며 각 분할에 대한 결과 봄

#### 1) Training :

* Few-shot ImageNet에서 동일한 훈련 하이퍼파라미터와 스케줄이 사용되었지만, COCO와 PASCAL VOC 클래스가 겹치기 때문에 이제 ImageNet에서 backborn을 사전 훈련하고, 각 반복은 1개의 쿼리 이미지와 15개의 예시 인스턴스로 구성된다는 점을 제외하면, Ablations와 동일

#### 2) Inference :

* 모든 분할에 대해 'Few-shot object detection via feature reweighting'에서 제공한 것과 동일한 예시를 사용하여 훈련 schedule이 끝날 때 얻은 모델을 사용하여 기본 및 신규 클래스 메트릭을 평가

#### 3) Baselines :

* 모델의 architecture의 차이를 더 잘 제정하기 위해 FewShot-YOLOv2, Meta R-CNN, RepMet을 훈련했지만 온라인 환경에서의 적합성을 평가하기 위해 few-shot exemplars에 대한 미세 조정은 하지 않음

<a href='https://ifh.cc/v-nokF8M' target='_blank'><img src='https://ifh.cc/g/nokF8M.png' border='0'></a>
#### TABLE 2

> AP50 scores on 20-way VOC test proposed by FewShot-YOLOv2

> 동일한 back born중 가장 우수한 신규 클래스 결과는 굵은 글씨로 표시

#### 4) Results :

* FewShot-YOLOv2, Meta R-CNN은 메타 학습되었지만 온라인 탐지를 수행하도록 설계되지 않아 새로운 보이지 않는 클래스에 대한 성능이 좋지 않음

* 이와 달리 R-101-DCN의 원래 RepMet 구현은 표에 표시된 RepMet의 바닐라 R-50-FPN 변형보다 큰 차이로 성능이 뛰어남

* 코사인의 기본 클래스 성능이 다른 메서드에 비해 약간 떨어지는 것을 알 수 있음

* 하지만 온라인 Few-Shot Mehod의 주요 목표는 새로운 클래스에서 좋은 성능을 내는 것이므로, 새로운 클래스 성능을 높이기 위한 합리적인 절충안으로 해석

* 유클리드 거리를 사용한 결과를 보면 코사인을 사용한 것보다 평균적으로 약간 떨어지는 것을 보아 코사인의 중요성이 보임

### Ablations

* 이상적인 상태에서 5-way ImageNet detection 결과를 비교하여 ablations on Cos R-CNN을 진행

* ablations의 경우 쿼리 이미지가 각각 1개씩 포함된 N개의 에피소드를 구성하여 모든 이미지를 평가
  > 여기서 N은 데이터 세트의 이미지 수임

* 이렇게 하면 포괄성을 잃지 않고 더 빠르게 평가

### 1) Cosine Form :

* 코사인 유사도 출력에 매개변수화된 scalar affine transformation(scale γ와 bias β의 형태)을 적용
* 이렇게 하면 코사인 기반 공식의 장점을 그대로 유지하면서 로짓이 [−1,1]에서 [−∞,∞] 사이에 있어야 한다는 제약을 무시 가능
* γ가 있는 경우 바이어스 계수 β는 그다지 영향을 미치지 않는 것으로 보이며, 약간 탐지 성능이 저하

### 2) Loss Obfective :

<a href='https://ifh.cc/v-PN3X1G' target='_blank'><img src='https://ifh.cc/g/PN3X1G.png' border='0'></a>
#### TABLE 3

  > Ablations on the cosine box head reported as AP5

<a href='https://ifh.cc/v-pMCV41' target='_blank'><img src='https://ifh.cc/g/pMCV41.png' border='0'></a>
#### TABLE 4

  > Cos RPN embedder ablations reported as AP50

* 두 표의 RoIs
  > 코사인 유사성 기반 소수 샷 감지의 경우 소프트맥스 손실이 더 우수한 결과를 제공한다는 것을 알 수 있음
  
  > 탐지 결과를 관찰하면 동일한 박스에 대해 모든 예시 클래스를 예측하는 경향이 있으며, 이는 분류율을 낮추고 배경 클래스를 억제하여 탐지 성능을 떨어뜨립니다.

### 3) Cos RPN :

* TABLE 4의 표에서 전반적인 추세로 볼 때, Cos RPN은 표준 RPN에 비해 few-shot detection하는데 최적이지 않은 것으로 보임

* 한 가지 가능한 설명은 물체의 모양이 너무 다양해서 단일 중심을 중심으로 안정적으로 클러스터링할 수 없기 때문에 코사인 유사성 공식이 가능한 모든 변화 모드를 포착하지 못하기 때문일 수 있음

* 또는 기본 훈련 데이터의 다양한 객체 모양이 표준 RPN이 보이지 않는 객체의 좋은 boundary box를 제안하기 충분할 수도 있기에 이 논문에서는 표준 RPN을 채택

* 하지만 표준 R-CNN 시스템의 표준 RPN이 객체성을 예측하는 동안, box head가 역전파하는 그라데이션의 혜택을 받아 새로운 클래스 객체에 대한 좋은 제안을 생성할 수 있는 Cos RPN의 표준 RPN도 있을 수 있음

* 또한 코사인 공식이 없으면 새로운 클래스의 온라인 탐지가 불가능

### 4) Su-MoCo

<a href='https://ifh.cc/v-nw5xRC' target='_blank'><img src='https://ifh.cc/g/nw5xRC.png' border='0'></a>
#### TABLE 5

* TABLE 5(a)표에 표시된 것처럼 Su-MoCo의 모멘텀 및 대기열 크기 하이퍼파라미터를 제거
* 대기열 크기가 커질수록 새로운 클래스에 대한 성능이 향상되는 것을 발견했으며, 이는 모델이 학습 반복 중에 더 많은 예시를 고려할 수 있으면 더 나은 특징 표현을 학습한다는 직관적인 사실을 확인시켜 줌
* 대기열 크기가 증가함에 따라 대기열의 오래된 예시가 여전히 정보를 제공하도록 하기 위해 예시와 경로 가중치가 더 느리게 진화해야 하므로 모멘텀도 증가해야 함
* Su-MoCo를 사용하지 않았을 때와 비교하여 새로운 클래스에서 전반적으로 2~4%의 성능 향상을 달성하여 Su-MoCo 도입의 효과를 보여줌

## Conclusion

* 이 논문에서는 Cos R-CNN online few-shot object detector를 제안하고 제거 연구를 통해 설계를 검증
* ImageNet 5-way few-shot detection 벤치마크에서 Cos R-CNN의 성능을 평가한 결과, 1/5/10 샷 설정에서 최신 기술을 8/4/1% 능가하는 동시에 더 간단한 포뮬러를 사용
* 이는 few-shot PAS-CAL VOC 벤치마크에서도 반영되어 새로운 클래스의 최신 방법을 최대 20%까지 앞섬










































