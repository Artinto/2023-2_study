# Autoencoder : Reducing the Dimensionality of Data with Neural Networks(2006)  
* Geoffrey Hinton(제프리 힌튼): 딥러닝의 대부
  * 볼츠만 머신 제안
  * XOR 적용 문제(Back Propagation, Multi-layer perceptron)
  * Deep Belief Nets
* Ruslan(Russ) Salakhutdinov(러슬란 살라쿠트디노브): 전 Apple ai 연구 디렉터

## Abstract
Autoencoder는 주로 차원 축소 및 특징 추출을 위해 사용되는 인공 신경망 구조이다. 
* 구조  
<img width="500" alt="image" src="https://github.com/ces0o/Paper-Review/assets/127365253/bd6c3ffa-8279-4c6e-bc80-215027cb0af4">

[출처](https://paperswithcode.com/method/autoencoder)  

</br>

* 인코더(Encoder)
  * 고차원의 입력 데이터를 저차원의 hidden state(은닉층,  coder, latent)로 변환하는 역할(압축)
  * 차원이 높을수록 모델의 복잡성과 학습에 필요한 데이터 양이 증가

</br>


* 디코더(Decoder)
   * 인코더가 만들어낸 저차원의 hidden state를 고차원의 출력 데이터로 복원하는 역할
   * 추출된 특징을 바탕으로 원본 데이터를 재구성
      * 완벽하게 복원을 못하지만, 최대한 가깝게 복원하고자함

</br>

* 코드(code 혹은 Latent space)
  * 인코더와 디코더의 출력과 입력으로 쓰이는 hidden state를 의미
  * 입력 데이터의 압축된 형태로 중요한 특징들만 존재

</br>

## 등장배경  
* 차원 축소와 특징 추출의 필요성
   * 고차원 데이터는 많은 정보를 포함하고 있지만 정보를 분석 및 해석이 어려움
   * 차원이 높을수록 모델의 복잡성과 학습에 필요한 데이터 양이 증가
* 고차원의 데이터 → 저차원 데이터
  * 계산 효율 증가
  * 데이터 분석 및 해석 용이(시각화, 분류)
* 차원의 저주(Curse of Dimensionality)
  * 데이터의 차원이 증가함에 따라 데이터의 개수가 차원이 크기보다 작아져 학습 효율이 떨어지는 현상  
  <img width="600" alt="image" src="https://github.com/ces0o/Paper-Review/assets/127365253/a9056b46-a3a6-4558-972c-f4c2731ff492">

  [출처](https://esj205.oopy.io/978eadf3-ddc3-4bd7-a5b1-f2f085ff7252)  
  </br>  
  * 차원이 증가할 수록 데이터가 특정 공간에 차지하는 공간이 작아짐
  * 모델을 학습함에 있어 필요한 데이터가 기하급수적으로 늘어남
  * 해결 방법
    * PCA와 같은 차원 축소 기법을 통한 데이터의 차원 축소
    * 훈련 샘플의 밀도가 충분히 높아질 때까지 데이터의 크기를 키움
  * KNN, SVM, GMM과 같은 기계학습 기반 알고리즘 학습 시 매우 안 좋은 영향

</br>

## Manifold Learning
* Manifold : 데이터가 있는 공간, 데이터들을 최대한 에러 없이 잘 아우를 수 있는 Subspace(부분공간)
* 이러한 Manifold들을 잘 찾는 것이 Manifold Learning
* Manifold Learning의 목적
  * Data compression : 데이터 압축
    * Code layer로 압축 후 이를 다시 Decoding 했을 때 원본 데이터로 잘 복원이 되면 잘 압축이 된 것
    * 입력 데이터를 차원을 축소하여 저차원의 데이터로 전환  
    <br>  
  * Data visualization : 데이터 시각화
    * 데이터에서 직관이나 해석을 쉽게 하기 위해 활용
    * t-SNE(t-분포 확률적 임베딩):  차원 축소 시 비슷한 구조끼리 데이터를 정리한 상태
    * Mnist에 대한 t-SNE의 결과  
    <img width="338" alt="image" src="https://github.com/ces0o/Paper-Review/assets/127365253/ee366228-025c-47d6-95ea-34d37a694758">

    [출처](https://towardsdatascience.com/an-introduction-to-t-sne-with-python-example-5a3a293108d1)     
    <br>  
  * Curse of dimensionality 개선 : 차원의 저주 개선
    * 차원의 저주 : 차원이 높아질수록 공간은 커지는 데, 데이터의 수는 고정되어 데이터의 밀도가 희박해지는 문제
    * Manifold Learning을 통해 저차원의 Manifold를 찾으면 데이터의 밀도가 높게 나타나짐    

    <br>  
  * Discovering most important features : 유용한 특징 추출
    * Manifold를 찾았다는 것 자체가 데이터에서 유용한 특징을 찾았다는 의미
    * Mnist의 이미지에 대한 Manifold를 찾았다면 해당 Manifold에는 이미지의 크기, 회전, 변형, 두께 등의 유의미한 Feature들을 찾을 수 있다
* Manifold의 실질적 의미  
   <img width="505" alt="image" src="https://github.com/ces0o/Paper-Review/assets/127365253/05b59eb0-fb9a-44b0-b8f3-369162d6fc50">  
   <br>

   * 위의 사진에서 3차원 데이터 분포를 볼 수 있다
   * 3차원의 데이터에서 Manifold두 점 사이의 거리로 가운데 점을 찾는 다면, Manifold위에 없는 데이터가 선택될 수 있고, 그 데이터를 보면 의미 없는 데이터일 수 있다
     * 위의 그림인 경우에 가운데의 이미지는 팔이 여러개인 데이터로 의미없는 데이터  
     
  </br>  

   <img width="548" alt="image" src="https://github.com/ces0o/Paper-Review/assets/127365253/f44844c1-123a-42e9-a786-72c8c1381823">

   * 하지만, Manifold 상에서 가운데 점을 찾는다면, 기대하는 의미가 있는 이미지가 나옴  
  * Manifold Learning을 위한 선형적 방법으로 PCA, 비선형적 방법으로 Auto-Encoder가 사용된다
  * 위에서 언급한 t-sne도 비선형적 방법  
  [참고 및 출처](https://gaussian37.github.io/dl-concept-autoencoder2/)

<br>

## Principle Component Analysis(PCA): 주성분 분석
* 당시에 대표적으로 dimensionality reduction(차원 축소)에 쓰이던 기법
* 고차원의 데이터 → 저차원의 데이터
* 데이터의 차원이란?
  * 아이리스 데이터에 대해 확인
    ```python
    # 데이터 불러오기
    from sklearn.datasets import load_iris
    import pandas as pd

    iris = load_iris()
    Iris_Data = pd.DataFrame(data=iris['data'], columns= iris['feature_names'])
    Iris_Data['target'] = pd.DataFrame(data=iris['target'],columns = ['target'])
    Iris_Data
    ```
  * 결과  
  <img width="367" alt="image" src="https://github.com/ces0o/Paper-Review/assets/127365253/5937ec62-45b8-4550-9c40-ea62bb98625d">
  
    * Sepal length, Sepal width, petal length, petal width 4개의 Feature(독립 변수)
    * 해당 데이터를 하나의 공간에 표현할 때 그 공간의 차원은 4차원이 되야함
  * 3개의 Feature에 대한 공간상에 표현
    ```python
    import matplotlib.pyplot as plt

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    xs = Iris_Data['sepal length (cm)']
    ys = Iris_Data['sepal width (cm)']
    zs = Iris_Data['petal length (cm)']
    color = Iris_Data['target']

    p = ax.scatter(xs, ys, zs, c=color, cmap='viridis')
    fig.colorbar(p)
    ax.set_xlabel('Sepal Length')
    ax.set_ylabel('Sepal Width')
    ax.set_zlabel('Petal Length')

    plt.show()
    ```
  * 결과  
    <img width="335" alt="image" src="https://github.com/ces0o/Paper-Review/assets/127365253/360a29fd-d451-40d7-88cb-717e7926cea0">

  * 하지만, 데이터의 차원이 커질수록 계산량이 증가 및 학습을 위해 요구되는 데이터의 sample의 수가 많아지고, 만약 부족하다면 공간이 불안정해짐
  * 모든 피처들 중 그 피처들을 잘 설명하는 하나의 축(주성분 축)이 있지 않을까? 의 의문에서 시작
  * 그러면 그 주성분 축에 이제 내적(정사영)을 하게 되면, 이 데이터 셋에 대해 잘 설명할 수 있는 벡터를 찾을 수 있다
  * 즉, 최대한 특징을 살리면서, 차원을 낮출 수 있다  
  
  </br>  

  * 주성분을 구하는 방법
    * 분산 : 데이터의 특정한 점과 데이터들의 평균과의 차이를 제곱한 값들의 평균
    * 분산이 크면 데이터들이 평균에서 멀리 떨어져 있다 → 중심에서 멀리 퍼져 있다 → 각 데이터들이 서로 다른 값들을 가지고 있다.(데이터 간의 차이가 크다.) → 데이터의 특성을 잘 표현한다
    * 분산이 가장 큰 방향이 주성분 방향  
      <img width="379" alt="image" src="https://github.com/ces0o/Paper-Review/assets/127365253/22703114-44c4-4162-9476-aeab9e4f8827">   
      [참고](https://darkpgmr.tistory.com/110)
    * 크기가 1인 임의의 단위 벡터(w)
    * 데이터의 계수가 n개, hi가 Zi를 w에 정사영 시킨 벡터. 입력 데이터들을 행벡터로 쌓아 생성한 행렬를 Z(n x p)
    * 분산(평균이 0)
      
    $$분산 =  \frac{1}{n}\sum_{i}^{} (z_i*w)^2 = \frac{1}{n}(Zw)^T(Zw) =  \frac{1}{n}w^TZ^TZw = w^TCw$$
    
    * 여기서 C는 공분산 행렬(covariance 행렬 $C = \frac{Z^TZ}{n}$)이 된다
    * w가 길이가 1인 단위 벡터이므로 $w^tw = 1$이 성립
    * Constrained Optimization(제약하의 최적화) : 특정 조건 내에서 최선의 결과를 도출하는 것(최적화)
      * 모든 x에 대해 f(x)를 찾는 것이 아니라, 일정한 제약 하의 x에 대해 함수값을 찾는 것
      * **Lagrange multiplier**을 이용해 최적화 문제로 식을 세울 수 있음
        * u를 최대화 하는 방법  
          $$u=w^TCw-\lambda(w^Tw-1)$$  
        * u를 w에 대해 미분  
          $$\frac{\partial u}{\partial w} = 2Cw - 2\lambda w =0$$  
          $$Cw = \lambda w$$
    * 공분산(Covariance matrix)
      * 두 벡터 사이에 어떠한 상관관계가 있는 확인  
         <img width="248" alt="image" src="https://github.com/ces0o/Paper-Review/assets/127365253/d88d7a14-75fb-4fcc-88c3-e3259f807344">  
       * 대각선 방향으로 x1의 분산, x2의 분산 … xd의 분산을 의미
       * 공분산 행렬은 데이터가 각 축에 대해 얼마나 퍼저 있는지를 담고 있음
    * 고유값과 고유벡터(eigenvalue, eigenvector)  
       $$Av = \lambda v (v \neq 0)$$
      * A는 n x n의 정방 행렬일때, v를 고유벡터, 람다를 고유값(상수)으로 정의  
        <img width="203" alt="image" src="https://github.com/ces0o/Paper-Review/assets/127365253/2446494f-214c-4bfe-9498-5ec782b8d81f">  
      * v의 고유벡터를 A로 선형변환(정상영)시킨 결과가 상수배라는 의미
      * 즉, 분산을 최대하는 하는 방향이 결국에 데이터의 주성분을 나타내는 방향이다
      * 여기서 람다가 w방향의 크기가 된다
      * PCA의 결과는 항상 선형적 결과
      * [자세한 내용](https://angeloyeo.github.io/2019/07/27/PCA.html)   
  * PCA 과정   
    <img width="379" alt="image" src="https://github.com/ces0o/Paper-Review/assets/127365253/1cfcc057-1b85-46e1-9049-78c4e2858627">  
      [출처](https://sagarsaha455.medium.com/pca-for-visualization-and-dimension-reduction-14492e2acf2b) 

<br>

## 다층 퍼셉트론(Multilayer Perceptron)  
<img width="418" alt="image" src="https://github.com/ces0o/Paper-Review/assets/127365253/8d12f767-32cb-4973-80ee-cc711bca68be">     

[출처](https://yhyun225.tistory.com/21)  
* 1층  
 * $$ L_1 = W_1 * x^T $$  
  
* 2층  
 * $$ L_2 = W_2 * L_1 = W_2 * W_1 * x^T $$
  
* 그러면, PCA에 다층 퍼셉트론처럼 비선형성을 추가할 수 없을까?  


## Auto-Encdoer
<img width="443" alt="image" src="https://github.com/ces0o/Paper-Review/assets/127365253/effd5b97-0f24-4f59-b9a3-ab0f98da04cf">  

### Pretraining
  * 딥러닝에서 초기값 설정이 매우 중요
  * 당시에 학습이 잘 되지 않았던 것은 우리가 초기화를 멍청한 방법으로 했다고 힐튼 교수님이 지적

#### 제한된 볼츠만 머신(Restricted Boltzmann machine)  
<img width="160" alt="image" src="https://github.com/ces0o/Paper-Review/assets/127365253/0c408d22-6968-4a72-9b80-efaadcaeab13">    

* Visible, Hidden의 두개의 Layer로, 두 레이어들이 양방향으로 전부 연결된(Fully Connected) 모델
* 훈련과정
  1. Forward : Input Data에 가중치를 이용해 Output을 만듦
  2. Backward : Ouput에 같은 가중치를 이용해 Input을 재생성(Recreate)
  3. 원래의 Input Data와 재생성된 Input의 값을 비교해 두 값이 최대한 비슷해지도록 가중치 업데이트

#### Deep Belif Network(DBN)
<img width="340" alt="image" src="https://github.com/ces0o/Paper-Review/assets/127365253/a797be82-0c31-40e8-97d8-6cf7d6828c57">  

[출처](https://www.analyticsvidhya.com/blog/2022/03/an-overview-of-deep-belief-network-dbn-in-deep-learning/)  

* RBM을 이용해 가중치를 초기화한 신경망
* 관련 자세한 내용
  * [A Fast Learning Algorithm Deep Belief Nets - Restricted Boltzmann Machine(RBM)](https://www.cs.toronto.edu/~hinton/absps/fastnc.pdf)
  

### 현재에서 사용은?
* 2010년의 Xavier 초기화 등장

  $$N(0, var=2/(n(in)+n(out)))$$
  
  * n(in) : 가중치에 입력으로 들어오는 뉴런의 수
  * n(out) : 가중치에서 출력으로 나가는 뉴런의 수
  * 입력 데이터와 출력 데이터 수에 맞게 가중치 행렬 생성 시 가우시안 분포에서 임의값을 추출하고, 그 값을 입력 데이터 수의 제곱근으로 나누어 사용
  * 따라서 가우시안 분포의 분산은 입력 뉴런의 수와 출력 뉴런의 수에 따라 동적으로 조절된다
  * Activation Function으로 Sigmoid나 Tanh 함수 사용 시 사용
* 2015년의 He’s 초기화 등장

  $$N(0, var=2/((1+a^2)*n(in))$$

  * a : ReLU 또는 Leaky ReLU의 음수부분의 기울기 (기본값 = 0)
  * 입력데이터 수의 절반의 제곱근으로 나누어서 사용
  * ReLU가 활성화 함수로 많이 사용되면서 활성화 값이 0이하인 경우에 발생하는 ReLU의 특징을 반영하기 위해 등장
  * Activation Function으로 ReLU 함수 사용 시 사용
* 위의 두가지 방법으로 인해서 현재는 RBM은 잘 사용하지 않음.
* [모두를 위한 딥러닝 시즌 1](https://www.youtube.com/watch?v=4rC0sWrp3Uw&list=PLlMkM4tgfjnLSOjrEJN31gZATbcj_MpUm&index=32)

## Continue
<img width="443" alt="image" src="https://github.com/ces0o/Paper-Review/assets/127365253/effd5b97-0f24-4f59-b9a3-ab0f98da04cf">    

* 위세서 RBM을 이용해서 각 요소에 대해서 학습을 진행 후 일렬로 쌓은 것이 **Auto-encoder**이다.
  * 500 -> 30 -> 500의 과정, 
  * 1000 -> 500 -> 1000의 과정
  * 2000 -> 1000 -> 2000의 과정
  * InputData -> 2000 -> OuputData의 과정
  * 위 과정을 결국에 쌓아다 표현해서 Stack Auto-encoder라고 말하기도 함.

<br>  

* Fine-tuning이 backpropagation을 통한 학습 과정을 의미
  * 이때 각 레이어에 대한 Weight들이 Update 됨.
* 특징 (Self-Supervised Learning)
  1. 자동으로 특징 학습
      * Autoencoder는 입력 데이터를 재구성(reconstruction)으로써 학습이 진행됨. 이 과정에서 중간에 있는 은닉층은 데이터의 특징을 추출하는데 도움이 되며, 이는 주어진 데이터의 표현을 자동으로 학습
  2. 비지도 학습
      * 입력 데이터가 타깃값
      * Autoencoder는 비지도 학습 방법 중 하나로, 레이블이 없는 데이터에서도 효과적인 학습 가능
</br>

## PCA vs Auto-Encoder
* 다음 결과들은 PCA와 Auto-Encoder를 비교하기 위해 곡면상의 데이터를 각각 PCA와 Auto-encoding시킨 결과 비교.

* PCA의 결과  
<img width="400" alt="image" src="https://github.com/ces0o/Paper-Review/assets/127365253/a3f77257-cb8c-44f7-b87c-1165fc5fbfef">  

* Auto-Encoder의 결과  
<img width="400" alt="image" src="https://github.com/ces0o/Paper-Review/assets/127365253/51be39af-1d93-4e01-a652-464a924cbf78">  

* x축(-1 ~ 3)  
<img width="400" alt="image" src="https://github.com/ces0o/Paper-Review/assets/127365253/0d5a24e5-d98f-4c19-908e-7f6e6e8ffaf8">  

* y축(-1 ~ 3)  
<img width="400" alt="image" src="https://github.com/ces0o/Paper-Review/assets/127365253/0d7be675-b4fd-47bc-8662-e06b08e097df">   

* [출처](https://www.youtube.com/watch?v=C21GoH0Y9AE)
* Auto-Encoder는 PCA와 달리 선형의 Manifold(평면)을 학습하는 것이 아니라 곡면을 학습할 수 있다. 
  * Swiss Roll 데이터에 대한 확인
  ```python
  # code for colab

  # Library import
  import numpy as np
  import matplotlib.pyplot as plt
  from mpl_toolkits.mplot3d import Axes3D
  from sklearn.decomposition import PCA
  from sklearn.datasets import make_swiss_roll
  from keras.layers import Input, Dense
  from keras.models import Model

  # Swiss_roll 데이터 생성.
  n_samples = 3000
  X, colors = make_swiss_roll(n_samples) 
  X = X.astype('float32') / 255.0
  # 생성된 데이터 확인
  fig = plt.figure(figsize=(6, 6))
  ax = fig.add_subplot(111, projection='3d')
  ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=colors)
  ax.set_title('Original Data')
  plt.show()
  
  # 학습
  # PCA 학습
  pca = PCA(n_components=2)
  X_pca = pca.fit_transform(X)

  # Auto-encoder 학습
  input_img = Input(shape=(3,))
  encoded = Dense(2, activation='relu')(input_img)
  decoded = Dense(3, activation='sigmoid')(encoded)
  autoencoder = Model(input_img, decoded)
  encoder = Model(input_img, encoded)
  autoencoder.compile(optimizer='adadelta', loss='binary_crossentropy')
  autoencoder.fit(X, X,
                  epochs=10,
                  batch_size=256,
                  shuffle=True,
                  validation_data=(X, X))
  X_auto = encoder.predict(X)

  # 결과 출력
  # 결과를 3차원으로 표현.
  fig = plt.figure(figsize=(12, 6))
  ax = fig.add_subplot(121, projection='3d')
  ax.scatter(X_pca[:, 0], X_pca[:, 1], colors, c=colors)
  ax.set_title('PCA')
  ax = fig.add_subplot(122, projection='3d')
  ax.scatter(X_auto[:, 0], X_auto[:, 1], colors, c=colors)
  ax.set_title('Autoencoder')
  plt.show()

  # 2차원으로 출력.
  fig2 = plt.figure(figsize=(12, 6))
  ax2 = fig2.add_subplot(121)
  ax2.scatter(X_pca[:, 0], X_pca[:, 1], c=colors)
  ax2.set_title('PCA')
  ax2 = fig2.add_subplot(122)
  ax2.scatter(X_auto[:, 0], X_auto[:, 1], c=colors)
  ax2.set_title('Autoencoder')
  plt.show()
  ```
  * 결과
    * 데이터  
    <img width="300" alt="image" src = "https://github.com/Sbeom12/study/blob/main/image/Auto_encoder/swissdata.png?raw=true">

    * PCA vs Auto_encoder  
    <img width="500" alt="image" src = "https://github.com/Sbeom12/study/blob/main/image/Auto_encoder/swissresult.png?raw=true">



## Result
* Image Reconstruction  
  <img width="500" alt="image" src="https://github.com/ces0o/Paper-Review/assets/127365253/e25149cb-9e77-4257-a31a-d381a3500d62">    
  A: Strokes Reconstruction, B: MNIST Reconstruction, C: Face Reconstruction

  A : Strokes Reconstruction
    * (28×28)-400–200–100–50–25–6 | 6-25-50-100-200-400-(28x28)로 생성
    * 6개의 Logistic PCA를 통한 생성
    * 18개의 logistic과 standard PCA를 이용한 학습
    * MSE는 각각 1.44, 7.64 2.45, 5.90으로 Auto-Encoder가 가장 뛰어난 성능
</br>

  B : MNIST Reconstruction
    * 784 - 1000 - 500 - 250 - 30의 Auto-endcoder, 30차원의 logstic PCA와 standard PCA의 결과
    * 각각 3.00, 8.01, 13.87의 average squared error  

  C : Fase Reconstrucition
    * 625 - 2000 - 1000 - 500 -30차원의 Auto-encoder와 PCA의 결과
    * 126, 135의 average squared error

* Mnist  
  <img width="500" alt="image" src="https://github.com/ces0o/Paper-Review/assets/127365253/e3603904-8775-464a-ac1f-38ab05e6effc">  

  A: First 2 PCA Components by PCA, B: 784–1000–500–250–2 autoencoder
    * randomly initialized backpropagation 1.6% error
    * 784-500-500-2000-10 pretrained는 1.2%
* Doucument Retrieval
<img width="500" alt="image" src="https://github.com/ces0o/Paper-Review/assets/127365253/128237b9-a806-4a0a-b39a-f594a1b4a421">

  A: Document Retrieval Accuracy, B: LSA, C: 2000–500–250–125–2 autoencoder
  * 잠재 의미 분석(Latent Semantic Analysis, LSA) : 텍스트 데이터의 차원 축소 및 문서와 단어 사이의 잠재적인 의미 추출

## Code
* Mnist에 대한 Auto-encoding 결과
  * 데이터 셋 불러오기
  ```python
  # code for colab
  import torch
  from torch import nn
  from torch.utils.data import DataLoader
  from torchvision import datasets, transforms
  import matplotlib.pyplot as plt

  # 데이터 셋 불러오기
  transform = transforms.Compose([transforms.ToTensor()])
  # Train 데이터
  train_dataset = datasets.MNIST(
      root="~/torch_datasets", train=True, transform=transform, download=True)
  train_loader = DataLoader(train_dataset, batch_size=128, shuffle=True)
  # Test 데이터
  test_dataset = datasets.MNIST(
      root='./data', train=False, download=True, transform=transform)
  test_loader = DataLoader(test_dataset, batch_size=10, shuffle=False)
  ```
  * Auto-Encdoer 설정
  ```python 
  # 모델 선언.
  class Autoencoder(nn.Module):
      def __init__(self):
          super(Autoencoder, self).__init__()

          self.encoder = nn.Sequential(
              nn.Linear(28 * 28, 128),
              nn.ReLU(inplace=True),
              nn.Linear(128, 64),
              nn.ReLU(inplace=True),
              nn.Linear(64, 12), 
              nn.ReLU(inplace=True), 
              nn.Linear(12, 3))

          self.decoder = nn.Sequential(
              nn.Linear(3, 12),
              nn.ReLU(inplace=True),
              nn.Linear(12, 64),
              nn.ReLU(inplace=True),
              nn.Linear(64, 128),
              nn.ReLU(inplace=True), 
              nn.Linear(128, 28 * 28), 
              nn.Sigmoid())

      def forward(self, x):
          x = self.encoder(x)
          x = self.decoder(x)
          return x
  ```
  * 학습
  ```python
  model = Autoencoder()
  criterion = nn.MSELoss()
  optimizer = torch.optim.AdamW(model.parameters(), lr=1e-3, weight_decay=1e-5)

  num_epochs = 20
  for epoch in range(num_epochs):
      for data in train_loader:
          img, _ = data
          img = img.view(img.size(0), -1)
          output = model(img)
          loss = criterion(output, img)
          
          optimizer.zero_grad()
          loss.backward()
          optimizer.step()
          
      print('epoch [{}/{}], loss:{:.4f}'.format(epoch+1, num_epochs, loss.item()))
  ```
  * 결과 출력
  ```python
  for i, data in enumerate(test_loader):
    images, labels = data
    images = images.view(images.size(0), -1)
    outputs = model(images)
  
  images = images.view(images.size(0), -1)
  outputs = model(images)
  fig, axes = plt.subplots(nrows=2, ncols=10, figsize=(20, 4)) 
  for i in range(10):
    axes[0, i].imshow(images[i].reshape(28, 28).numpy())
    axes[1, i].imshow(outputs[i].reshape(28, 28).detach().numpy())
    axes[0, i].axis('off')
    axes[1, i].axis('off')
  plt.show()
  ```
  * 결과 
  <img width="500" alt="image" src = "https://github.com/Sbeom12/study/blob/main/image/Auto_encoder/mnistresult.png?raw=true">

