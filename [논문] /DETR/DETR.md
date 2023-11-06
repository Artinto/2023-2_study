# **DETR (2020)**  
---
End-to-End Object Detection with Transformers  
Review.LSJ, 2023.11.05  
## **Abstract**  
* 최초로 Transformer를 object detection에 적용. transformer encoder-decoder architecture
* object detection을 direct set prediction problem으로 간주-> bipartite matching을 통해 유니크한 예측
* hand-designed component인 NMS, anchor generation 등을 제거해 파이프 라인 간소화  

## **Background Knowledge**
### **Transformer**  
* **기존의 NLP 분야는 RNN을 자주 이용**  
  > 단점 1 : long-term dependecy problems, 앞에 있는 객체의 영향력 손실  
  > 단점 2 : RNN은 각 단어에 대한 전파력이 앞 방향으로만 있으므로 모든 단어들 간의 관계성을 파악하기 힘듦
  > -> 기존 RNN 모델들은 Attention 기법을 같이 엮어서 활용했음
* **Transformer는 RNN을 이용하지 않고 오직 Attention만을 이용해 NLP task 수행**
  * Attention이란 단어를 개별적으로 input 하는 것이 아닌 sentence 단위로 input하는 word embedding하는 것과 같음  
    > embedding이란?  
    > 단어를 벡터로 표현하는 방법. 밀집 표현으로 변환.
    > Q(Query) : Word matrix(단어 행렬), K(Key) : Similarity matrix(유사도 행렬), V(Value) : Weight matrix(가중치 행렬)
### **Hungarian Algorithm**  
* **두 집합 사이의 일대일 대응 시 가장 비용이 적게 드는 bipartite matching(이분 매칭)을 찾는 알고리즘**
  > 어떠한 집합 I와 matching 대상인 집합 J가 있을 때 ,i∈I를 j∈J에 matching하는데 드는 비용을 c(i,j)라 정의
  > σ:I → J로의 일대일 대응 중에서 가장 적은 cost가 드는 matching에 대한 permutation σ 찾음
  > > σ : matching 시 최적의 순서에 대한 index
  > ![image](https://github.com/sj990710/Thesis_Review/assets/127752372/0844f21b-f979-43a0-91d6-f858ba7a58f9)
  > > 행 : predicted bounding box, 열 : ground truth, 각 요소 : 행열이 matching 되었을 때의 cost
  > ![image](https://github.com/sj990710/Thesis_Review/assets/127752372/e1db901e-657f-4e6a-9e0a-9bb18651cec9)
  > > Fig3과 Fig4를 비교했을 때 Fig4의 matching cost가 더 작음

## **Introduction**  
* ### **기존 object detection은 pre-defined anchor 사용**  
  > - 이미지 내 고정된 지점마다 다양한 scale, aspect ratio 가진 anchor 생성  
  > - 해당 anchor를 기반으로 생성한 예측된 bounding boux와 ground truth match  
  > - IoU > threshold : positive, IoU <threshold : negeative. positive sample에 한해 bounding box regression 수행  
  > - threshold를 기준으로 독립적인 prediction을 수행하므로 하나의 groud truth에 다수의 bounding box가 매칭되는 many-to-one 관계 성립  
![image](https://github.com/sj990710/Thesis_Review/assets/127752372/80e5cf8c-f9b1-4b33-8eb0-56a6f1e0ebb6)

  > - 다수의 anchor 생성하므로 다양한 크기와 형태의 객체 효과적으로 포착 가능
  > - 하나의 ground truth를 예측하는 다수의 bounding box -> near-duplicate/redundant한 예측 존재
  > - 이를 제거하기 위해 NMS(Non Maximum Suppression)과 같은
* ### **DETR은 hand-crafted anchor 사용하지 않음**
  > - 하나의 ground truth에 오직 하나의 예측된 bounding box만 matching
  > - Ground truth를 예측하는 bounding box가 오직 하나인 one-to-one 관계이므로 post-processing 과정이 필요하지 않음
![image](https://github.com/sj990710/Thesis_Review/assets/127752372/40e3dafc-e24b-4b20-a319-7c6181e6f474)

## **The DETR Model**
### **Object Detection Set Prediction Loss**
![image](https://github.com/sj990710/Thesis_Review/assets/127752372/d2245d4e-a6c2-47e9-95c9-691facfb9b28)
  > L_match : prediction과 ground truth 사이의 pair-wise matching cost->N개의 예측들과 ground truth가 어떻게 매칭되어야 최소가 되는지 찾는 과정
![image](https://github.com/sj990710/Thesis_Review/assets/127752372/0b9e743c-66ac-4978-ac36-1a9b974b42fe)
  > 찾은 모든 pair에 Hungarian loss를 취함. Time complexity 완화.
### **DETR architecture**  
![image](https://github.com/sj990710/Thesis_Review/assets/127752372/c9fe9fb0-6fb7-498e-9354-7840caaa1b79)   
* **Transformer encoder-decoder attention**
  > 각 N개의 object queries(학습이 가능한 positional embedding)가 존재할 때 그들을 각각 병렬적으로 decoding
  > 해당 정보들이 기본적으로 하나의 인스턴스(Class가 같더라도 개별적인 사물)가 되어 predict
## **Result**  
![image](https://github.com/sj990710/Thesis_Review/assets/127752372/09ebe37c-3f12-49ea-860a-24ac527531a1)

## **장단점**  
* 장점
  > Faster R-CNN과 비슷한 성능인데 크기가 큰 객체를 훨씬 잘 포착함
  > customized된 layers를 따로 정해줄 필요없이 손쉽게 standard CNN과 transformer 구조를 사용
* 단점
  > 작은 object를 잘 탐지하지 못 함
  > Flop이 많아 학습시 많은 시간이 소요됨

