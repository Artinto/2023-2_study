# Cos R-CNN for Online Few-shot Object Detection

## Abstract
* Cos R-CNN, R-CNN formulation is designed for online few-shot object detection
* Cos R-CNN frames detection as a learning-to-compare task
* The cosine-based classification head allows for dynamic adaptation of classification parameters to the exemplar embedding
* The cosine-based encourages the clustering of similar classes in embedding space without the need for manual tuning of distance-metric hyper parameters
* Use a simple formula

## Introduction
* Deep Model을 학습하는데 있어 많은 양의 학습 데이터가 필요함
* 이에 대해 Few-shot learning에 대한 연구가 증가하는 추세
* 예제를 사용하여 기본 탐지기를 훈련한 다음 데이터가 부족한 새로운 클래스 예제를 사용하여 기본 탐지기를 미세 조정하는 2단계 훈련 파이프라인에 의존하고 있음
* 이 접근 성공적이지만, 임베디드 디바이스와 같이 리소스가 제한된 애플리케이션에 배포하는 데는 적합하지 않음
* Fig. 1과 같이 Few-shot learning은 미세 조정 없이도 보이지 않는 클래스를 감지할 수 있는 모델을 훈련 할 수 있음
* Cos R-CNN은 R-CNN의 일반적인 구조를 따르지만, 알려진 레이블의 예시와 유사한 객체의 위치를 생성하도록 학습
* 최근 Few-shot learning clasification의 접근 방식은 코사인 거리를 사용하는데 있어 모든 클래스의 로직을 동일한 범위로 확장하기 때문에 코사인 거리를 유사성 측정값으로 사용
* 코사인 기반 메트릭 학습은 각 반복에서 많은 양의 데이터를 표시할 때 이점을 얻을 수 있음
* R-CNN 기반 프레임워크는 작은 배치크기에서도 훈련 중에 큰 메모리 공간을 차지하기 때문에 일반적으로 이러한 공간을 차지하기 때문에 일반적으로 이러한 이점을 얻기가 어려움
* 이 문제를 해결하기 위해 훨씬더 큰 규모의 예시 코퍼를 비교하여 학습 프로세스를 개선할 수 있는 MoCo의 변형인 Su-MoCo도 도입
<a href='https://ifh.cc/v-fqRYKJ' target='_blank'><img src='https://ifh.cc/g/fqRYKJ.jpg' border='0'></a>
#### Fig. 1
