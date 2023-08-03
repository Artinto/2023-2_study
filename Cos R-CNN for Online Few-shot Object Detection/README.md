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

 > 각 m 클래스에 대해 n개의 예시를 제공. 그런 다음 추론은 n - m-방향, 1샷 검출로 이어짐. 그러나 소프트맥스를 n - m개의 예시 전체에 걸쳐 코사인 유사도 로그에 적용한 후, 각 클래스에 대한 탐지 점수는 동일한 클래스에 속하는 n개의 예시에서 얻은 점수의 합으로 계산

* m-way, n-shot task에서 클래스 i의 후행은 다음과 같이 주어짐

$$
p(y=i|x) = \frac{\sum_{k}^n exp(c'<sub>j</sub>)}{exp(\phi<sub>{bg}</sub>(x)) + \sum_{j}^n \sum_{k}^n exmp(c'<sub>jk</sub>)}
$$

* comparator-based classification의 경우 테스트에 사용된 것과 동일한 수의 샷(n)으로 훈련하는 것이 유리함

### C. Supervised Momentum Contrast(Su-MoCo)












