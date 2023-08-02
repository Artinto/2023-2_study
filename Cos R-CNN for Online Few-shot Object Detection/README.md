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

### Few-shot Classification
* 최근 등장한 개념은 메타 학습으로, 모델이 몇개의 짧은 작업으로 구성된 '에피소드'를 반복하여 학습하도록 설정하는 방식
* 단발성 작업의 분포를 학습함으로써 향후 발생할 수 있는 모든 단발성 작업으로 일반화하는 것을 목표
* Prototypical Networks와 Relation Networks 전략은 Few-shot Learning에서 유용하게 사용될 수 있는 전략
  > Protypical Networks : 쿼리 임베딩과 메타학습된 클래스 프로토타입 간의 유클리드 거리를 비교하여 가장 가까운 쌍을 매칭
  > Relation Networks : Prototypical Networks를 확장하여 유사도 측정 방법을 학습 가능한 관계 모듈을 도입하여 수행

### Few-shot Object Detection
* 대부분의 방법은 풍부한 기본 클래스에 대해 먼저 base detector를 훈련한 다음 부족한 새로운 클래스에 대해 미세 조정하는 2-stage training pipeline을 제안
* 최근 FSDet에서 가중치를 동결하고 R-CNN 검출기의 마지막 박스 헤드 레이어만 미세 조정하는 간단한 전략이 많은 최신 Few-shot Object detection 방법에 비해 우수
* 이와 관련된 모델로는 Fewshot-YOLOv2, Meta-RCNN, MetaDet, RepMet이 존재

## cos R-CNN
<a href='https://ifh.cc/v-9tgJzj' target='_blank'><img src='https://ifh.cc/g/9tgJzj.jpg' border='0'></a>
#### Fig. 2 (cos R-CNN architecture)
* 일반화를 위해 중요한 것은 동일한 객체 유형의 다양한 예제를 통해 학습한다는 점입니다.
* 신중한 정규화 없이 새로운 클래스를 탐지하기 위해 학습을 시도하면 소수의 특정 예제에 과적합할 가능성이 높기 때문에 이 공식은 소수 샷 탐지에는 적합하지 않음








