# Deep Residual Learning for Image Recognition
---
* [관련논문](https://arxiv.org/pdf/1512.03385.pdf)
* ILSVRC(ImageNet Large Scale Visual Recognition Challenge) 2015 대회에서 1등을 차지한 모델.  
    <img src= "https://miro.medium.com/v2/resize:fit:720/format:webp/1*Io-I-fOM0jGftDb_nne4KQ.png" width='500' hegith = '400'>  
    [출처](https://medium.com/@Lidinwise/the-revolution-of-depth-facf174924f5)
    * layer의 수가 VGG의 8배 깊음.
    * 정확도 3.57%
</br>

## Intro.
* Resnet이라는 이전까지 `깊이를 깊게 쌓을 수록 성능이 좋아진다`라는 인식을 기반으로 수많은 연구진들이 연구를 해옴.
    * Going deeper with convolutions. In CVPR, 2015.
    * Very deep convolutional networks for large-scale image recognition. In ICLR, 2015.
 
 </br>
    
* `Gradient Vanishing/Exploding`로 인해서 깊게 쌓기만 하는것은 마냥 쉬운 일이 아니였음.
    * Gradient Vanishing(기울기 소실) 문제는 Backpropagation(역전파) 과정에서 **Input layer로 갈수록 Gradient(기울기)가 점차적으로 작아지는 현상**.
        * layer 수가 많을수록 즉 깊이가 깊어질수록 문제가 심해짐.
    * Gradient Exploding(기울기 폭주) 문제는 소실과는 다르게 Backpropagation(역전파) 과정에서 **큰 값을 가지는 weight(가중치)들이 반복적으로 곱해져 weight(가중치)가 제대로 업데이트 되지 않는 현상**.
 
 </br>
    
* 기존 구조에서 레이어 깊이에 따른 학습 비교  
    <img src= "https://i.imgur.com/HIbfAlP.png" width='600' hegith = '300'>  
    * 레이어 수가 높을수록 오히려 성능이 degradation(약화)됨.
    * 이때 레이어 수가 높다고 overfitting이 된것이 아님.
</br>

## Residual Learning
* 연구진들은 Layer의 수를 깊게 하면서 깊이에 따른 학습 효과를 얻을수 있도록 Residual Learning을 고안함.  
    <img src= "https://i.imgur.com/mHfZYPQ.png" width='400' hegith = '300'>  
    * 기존 방식에서 input으로 x가 들어가 2개의 layer를 거쳐 출력으로 H(x)가 나오는 구조.
        * 목표 : 학습을 통해서 최적의 출력인 H(x)를 구하는 것이 목표
        * layer들의 파라미터들도 최적의 H(x)를 위해 결정됨.
    
    </br>

    * 하지만 기존 방식에서 H(x)를 얻는 것이 아닌 H(x) - x, 즉 출력과 입력의 차(Residual)를 얻을 수 있도록 관점을 바꿈.
        * layer는 H(x) - x를 얻도록 학습. 
        * F(x) = H(x) -x 
        * 출력은 H(x) = F(x)+x 가 된다.
        * 그러면, 블록을 오른쪽처럼 바뀌게 된다.
    
    </br>

    * Residual 구조
        * 입력에서 바로 출력으로 연결되는 shortcut 연결이 생성.
        * 계산량도 이전 방법과 큰 차이가 없음.
            * 덧셈 추가
        * pre-conditioning(사전조건화)
            * Residual 구조에서 최적의 목표값은 F(x)가 0인경우.
            * H(x) = x로 mapping하는 것이 학습의 목표.
            * 학습할 방향이 미리 정해짐.
        * 입력의 작은 움직임 검출
            * F(x)가 0에 가깝게 학습되므로 조금만한 x값의 변화에 의해 영향을 받게 됨.
    
    </br>

    * 효과
        * **Layer 수가 많은 깊은 망들도 최적화가 가능하다.(학습이 가능)**
        * **Layer 수가 늘어나 정확도가 개선된다.**

## Identity Mapping by shortcuts
* ResNet은 깊은 신경망을 효과적으로 학습시키기 위한 아키텍처로, 그 중요한 부분 중 하나가 residual block이다.
* 기본적인 **residual block의 구조**는 다음과 같다
    1. 입력 x에 대한 **합성곱(Convolution) 연산**과 **활성화 함수**를 적용한다.
    2. 이를 또 다른 합성곱과 활성화 함수를 거친 **출력에 더한다**.

</br>

### Indentity shortcut
$$ y= F(x, {W_i})+x$$

* 위 식에서 x와 y는 각각 input, output을 나타낸다. 잔차 학습을 이용하여 output 값에 input값인 x를 더해주는 것을 확인할 수 있다.
* 첫 번째 term은 학습된 residual mapping이다
* F + x 연산이 shortcut connection을 의미하고 element-wise addition이다.
* 위 식은 $F = W_2 \sigma(W_1x)$ 을 간소화한 모양으로 활성함수인 ReLU를 한 번 통과하고 biases는 생략된 식이다.

### Projection shortcut
* 만약 입력과 출력의 차원이 다르다면 덧셈 연산이 불가능하여 이를 해결하기 위해 Projection Shortcut을 도입하였다. 

$$ y = F(x, {W_i}) + W_sx $$

</br>

* 단순히 identity shortcut에서 **linear함수**인 $W_s$를 x에 곱한 꼴로 표현된다.
* **x와 F의 차원을 동일하게 맞춰주기 위해** 위의 식을 사용한다. 이를 통해 **입력값의 차원을 변환**하여 덧셈 연산이 가능하게 해준다.
* 또한 gradient를 구하였을 때 $W_s$가 사라지지 않고 남기 때문에 **vanishing gradient 문제를 해결** 할 수 있다.

</br>

* 이러한 구조를 통해 ResNet은 매우 깊은 네트워크에서도 안정적으로 학습이 가능하며, 그 성능은 다양한 computer vision task에서 입증되었다.

</br>

## Architecture(VGG19 vs Plain vs ResNet)
* 본 논문에서는 다음과 같이 모델들을 비교하고 있다.  
![image](https://github.com/Sbeom12/study/blob/main/image/Resnet/architecture1.JPG?raw=true)


### VGG19
![image2](https://production-media.paperswithcode.com/methods/vgg_7mT4DML.png)

* VGG-19는 19개의 계층으로 이루어진 깊은 컨볼루션 신경망(CNN)으로, 2014년 ILSVRC에서 사용된 모델 중 하나 이다. 주로 이미지 분류 작업에 적용되며, 작은 3x3 필터를 사용한 깊은 구조를 통해 복잡한 이미지 특징을 학습한다.

</br>

* 구조
    1. **13 Convolution Layers + 3 Fully-connected Layers**
    2. **3x3 convolution filiters**
    3. **stride: 1 & padding: 1**
    4. **2x2 max pooling (stride: 2)**
    5. **ReLU**

</br>

### Plain Network 
* **VGG net을 참고**해서 만든 Network로 conv filter의 사이즈가 3 x 3이고, 다음 2가지 규칙에 기반하여 설계하였다. 
    1. feature map의 size가 같은 layer들은 **모두 같은 수의 conv filter**를 사용
    2. **feature map 사이즈가 절반이 되면 filter 수는 2배**가 되도록 설계되었다.

![Alt text](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fbp8rUK%2FbtqS9ZghSdh%2F0JZUWVEjQT8E7wkRRY1W41%2Fimg.png)

* downsampling시 pooling 대신 stride가 2인 conv filter를 사용.
* 모델 마지막에 Global Average Pooling을 사용.
* 최종 레이어는 34개로, VGG19와 비교했을 때 **비교적 적은 filter와 복잡도**를 가지는 것을 확인할 수 있다.

### Residual Network
* **Plain net을 바탕**으로 설계된 Network이다. Plain net에서 **shortcut connection**이 추가되었다고 볼 수 있다.
![Alt text1](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fdek2kD%2FbtqTfCx4XTn%2FkMHkA7Fv8vbW5Hkmg1x3a0%2Fimg.png
)
이 때 Identity Shortcut은 input과 output을 **같은 차원**으로 맞춰줘야 한다. 차원을 맞추기 위해 **세 가지 방법**을 사용할 수 있다.

1. **Padding**
    - 차원을 조절하기 위해 0을 넣어서 맞춰준다.(zero-padding) → 추가 파라미터 없음.
2. **차원이 달라지는 점선 shortcut에만 1x1 convolution layer 적용**
    - 크기가 같은 실선의 identity shortcut은 그냥 더하고, **크기가 달라지는 점선 shortcut**에 대해서만 **1x1convolution layer**를 거쳐 크기를 맞춰준다.
3. **점선, 실선 상관 없이 모든 shortcut에 대해 1x1 convolution layer 적용**
    - **모든 shortcut**에 대해 **convolution layer**를 거쳐 크기를 맞춰준다.

![Alt text](https://github.com/Sbeom12/study/blob/main/image/Resnet/architecture2.JPG?raw=true)


||VGG19|Plain|Residual|
|:---|:------:|:---:|:---:|
|Parameter|19|34|34|
|FLOPs|19.6 billion|3.6 billion|3.6 billion|

</br>

## Results
* 18-layer와 34-layer에 대한 Plain network와 Residual network의 실험결과를 살펴보면 다음과 같다.
![결과1.JPG](https://github.com/Sbeom12/study/blob/main/image/Resnet/%EA%B2%B0%EA%B3%BC1.JPG?raw=true)
- Plain network이 경우는 18-layer가 결과가 좋고 Residual Network의 경우 34-layer가 더 좋다는 것을 볼 수 있다.
- **Convergence(수렴) 속도가 Residual Net의 수렴 속도가 더 빠르다는 것을 볼 수 있다.**

## Bottleneck
* 학습에 걸리는 시간을 고려하여 Layer 수가 50이 넘는 구조들에 대해 Residual Network를 아래와 같이 변경했다.
![](https://github.com/Sbeom12/study/blob/main/image/Resnet/%EA%B2%B0%EA%B3%BC2.JPG?raw=true)
- 기본적으로 차원을 줄였다고 나중에 다시 늘리는 구조.
    - 연산 시간 감소를 위해 사용.
    - 계산량을 줄이기 위해 사용.

|| Residual Network  | Bottlenet Network |
|---| :---: | :---: |
|파라미터 수| 3x3x64x2 = 1152|1x1x64+3x3x64+1x1x256 = 896|
* 파라미터 수가 22% 감소  

</br>

![](https://github.com/Sbeom12/study/blob/main/image/Resnet/%EA%B2%B0%EA%B3%BC3.JPG?raw=true)

- 위의 표는 single model에 대한 실험 표로 B와 C에서 B는 차원을 증가시키는 경우에만 projection shorcut을  나머지 shortcut에는 identity를 사용했고, C는 모든 shortcut에 projection shortcut을 사용한 경우이다.
- Resnet의 34만 사용해도 다른 모델들과 비교해도 될 정도로 강력했지만, 152-layer의 모델 2개 등 총 6개의 모델로 결합하여 최종적으로 3.57%의 오차율로 대회 1위를 달성했다.

</br>

## CIFAR-10의 데이터의 결과
- ILRSVRC 대회와는 다르게 이미지의 크기가 32x32라서 초기 7x7 conv를 3x3 conv연산으로 바꾸어 학습을 진행했고, 아래 그림과 같이 비슷한 경향을 가지는 결과를 얻었다.  
![](https://github.com/Sbeom12/study/blob/main/image/Resnet/%EA%B2%B0%EA%B3%BC4.JPG?raw=true)  


- Plain은 일정 layer의 수를 넘으면 그 이후의 layer부터는 성능이 좋지 않고, Residual은 layer의 수가 증가하더라도 결과가 더 좋아 지는 것을 확인할 수 있지만, 너무 크게 증가한 경우에는 더 좋지 않았다.
- 1202-layer의 결과
    - 학습을 진행할 때 최적화에 별 다른 어려움이 없음.
    - CIFAR-10의 데이터가 많지 않음.
    - maxout/dropout을 사용하지 않았음.
    - overfitting이 발생했다고 해석할 수 있다.

</br>

- 이에 Identity Mappings in Deep Residual Networks 2016년에 추가 연구 진행 및 발표.
- Pre-activation을 통해 개선.  
![](https://github.com/Sbeom12/study/blob/main/image/Resnet/%EA%B2%B0%EA%B3%BC6.JPG?raw=true)
    - 일반화 성능 향상.
    - 최적화가 쉬워짐.
- Residual 망이 layer-1000이 넘어가도 효과적으로 작동한다.  
- ![](https://github.com/Sbeom12/study/blob/main/image/Resnet/%EA%B2%B0%EA%B3%BC5.JPG?raw=true)  


## 추가 조사

### [Residual Networks Behave Like Ensembles of Relatively Shallow Networks](https://arxiv.org/pdf/1605.06431.pdf)
- Residual의 구조는 Ensemble(앙상블) 모델 처럼 작동한다.  

![](https://github.com/Sbeom12/study/blob/main/image/Resnet/%EC%95%99%EC%83%81%EB%B8%94.JPG?raw=true)
- 3개의 Convolution layer에 대한 구조를 다른 시점에서 바라본것.

#### Lesion Study(손상 연구)
* 학습된 ResNet에서 skip connection과  downsampling projection을 제외한 블록을 제거시키고 실험.  
<img src= "https://github.com/Sbeom12/study/blob/main/image/Resnet/%EC%86%90%EC%8B%A4.JPG?raw=true" width='400' hegith = '200'>   
<img src= "https://github.com/Sbeom12/study/blob/main/image/Resnet/%EC%B6%94%EA%B0%80%EA%B2%B0%EA%B3%BC1.JPG?raw=true" width='600' hegith = '400'>     

- VGG과 Resnet을 비교하면, VGG는 layer의 손실이 Error에 크게 영향주지만, Resnet는 Downsampling layer를 제외하고는 크게 영향을 주지 않음.
- 이는 VGG는 layer들간의 길이 unique하여 하나라도 지워지면 정보 손실이 심각해지지만, Resnet은 Unraveled의 관점에서 봤을 때 가능한 Path가 절반으로 감소하는 효과.
- Path들이 서로 Independent(독립적).
- Ensemble(앙상블)의 특징
    - 모델의 output은 ensemble된 model의 개수에 ‘smooth’하게 dependent.
- Residual network=  Ensenble?
    - Resnet의 layer를 감소 및 순서를 섞은 경우.   

<img src= "https://github.com/Sbeom12/study/blob/main/image/Resnet/%EC%86%90%EC%8B%A42.JPG?raw=true" width='500' hegith = '200'>   

- layer의 수가 감소할수록 Error는 smooth하게 증가.
- layer의 순서를 많이 바꿀수록  Error가 smooth하게 증가.
- 즉, Residual network은 Ensenble(앙상블)로 볼 수 있다.

#### Path  
<img src= "https://github.com/Sbeom12/study/blob/main/image/Resnet/%EA%B8%B8%EC%9D%B4.JPG?raw=true" width='800' hegith = '400'>     

- 95% 이상의 path가 19~35개의 모듈을 지남.
- path의 길이가 질수록 input의 영향을 적게 받게됨.
- 20개 보다 긴 경로들은 학습에 영향을 주기엔 너무 깊음.
- 즉, Residual network에서 학습에 영향을 주는 path들은 상대적으로 얕다.
- 또한, 역전파 과정에서 gradient 업데이트가 대부분 5개에서 17개의 길이에서 나옴.(전체의 약 45%정도로 effective path로 정의.)

#### Result
- Effective path만 학습 시킨 결과로 5.96%의 에러이지만, 전체를 학습 시킨 결과는 6.10의 에러.
- 오히려 더 좋은 결과.  

<img src= "https://github.com/Sbeom12/study/blob/main/image/Resnet/%EA%B8%B8%EC%9D%B42.JPG?raw=true" width='500' hegith = '200'>   

- Resnet에서 residual block을 제거했을 때 path length들이 얼마나 남아 있는지 진행한 실험.
- block을 제거하면 대부분 long-path들에 영향을 주고, layer을 제거했을 때는 여전히 effective path들이 남아있어서 error가 크게 증가하지 않지만, 20개를 제거했을 때는 effective path가 많이 지워져 error가 크게 증가하는 것을 볼 수 있다.
- 결론
    - Resnet은 이전 모델들에 비해 깊지만, 단일한 깊은 네트위크가 아닌 많은 경로들의 집합으로 볼 수 있음.
    - Backpropagation 중에 gradient에 기여하는 네트워크의 경로는 생각보다 얕다.
    - 즉, **Vanishing gradient를 완전히 해결할 수 없다.**

</br>

## BottleNet의 단점
- 1x1의 Convolution 사용
    - 구글의 Inception에서 사용되면서 주목.
    - 채널 수 조절, 계산량 감소, 비선형성 추가.
- 1x1의 convolution의 단점.
    - 강제로 채널을 줄여 정보 손실이 방생하여 정확도가 떨어진다.

* Inception vs xception
    * Xception은 Inception에 있는 1x1 conv 연산을 줄여 더 높은 정확도를 얻음.
    <img src= "https://github.com/Sbeom12/study/blob/main/image/Resnet/%EC%9D%B8%EC%85%89%EC%85%98.JPG?raw=true" width='400' hegith = '200'>   
    <img src= "https://github.com/Sbeom12/study/blob/main/image/Resnet/xception.JPG?raw=true" width='400' hegith = '200'> 

### 결과
<img src= "https://github.com/Sbeom12/study/blob/main/image/Resnet/%EC%9D%B8%EC%85%89%EC%85%98%20%EA%B2%B0%EA%B3%BC.JPG?raw=true" width='400' hegith = '100'>   

<img src= "https://github.com/Sbeom12/study/blob/main/image/Resnet/%EC%9D%B8%EC%85%89%EC%85%98%20%EA%B2%B0%EA%B3%BC2.JPG?raw=true" width='400' hegith = '100'>

* Xception이 Inception보다 조금 더 좋고, 파라미터수가 더 적은 것을 볼수 있지만, 속도는 조금 더 느리다.
* 자세한 내용은[Deep Learning with Depthwise Separable Convolutions](https://arxiv.org/pdf/1610.02357.pdf)

</br>

## 후속연구 : ResNext
[Aggregated Residual Transformations for Deep Neural Networks](https://arxiv.org/abs/1611.05431)  
* ResNext는 ResNet의 bottle neck을 아래 그림과 같이 수정한 것이다.
<img src= "https://github.com/Sbeom12/study/blob/main/image/Resnet/Resnext1.JPG?raw=true" width='400' hegith = '100'>   

* 왼쪽은 기존의 resnet 구조이고 오른쪽은 resnext 구조이다. 
* 구조
    1. 256개의 채널이 1x1 conv를 거쳐 128개의 채널이 되고, 
    2. 128개의 채널을 32개의 그룹으로 분할하여 각 그룹당 4개의 채널을 가짐
    3. 그 다음 32개의 그룹에서 생성한 4개의 피쳐맵을 연결하여 128개의 채널을 만든다.
    4. 마지막으로 1x1 conv를 거쳐서 256개의 채널이 생성된다. 
    * group의 개수, 즉 여기서 32는 이 논문에서 새로 도입된 개념인 **cardinality**가 된다.

### ****Cardinality vs Width****
- 위 논문에서는 ResNext에서 Width보다 Cardinality를 증가시키는 것이 더 효율적이라고 말한다.
    <img src= "https://github.com/Sbeom12/study/blob/main/image/Resnet/ResNext2.JPG?raw=true" width='400' hegith = '100'>  

    - 위의 표에서 d는 각 그룹의 채널 수를 의미한다. 32개의 그룹 (Cardinality)가 4개의 채널을 가졌을 때 더 성능이 향상된 것을 확인할 수 있다.
    - 즉, Cardinality가 높을수록 더 좋은 성능을 가지는 것을 볼 수 있다.

### Increasing Cardinality vs Deeper/Wider
* 위 논문은 마찬가지로 모델의 깊이나 넓이를 증가시키는 것 보다 Cardinality를 증가시키는 것이 더 효율적이라고 말하고있다.

    <img src= "https://github.com/Sbeom12/study/blob/main/image/Resnet/Resnext3.JPG?raw=true" width='400' hegith = '100'> 

* 위의 표에서는 ResNext-101 > ResNet-101 wider > ResNet-200 순으로 성능이 좋은 것을 확인할 수 있다. 따라서 cardinality > width > deep 순으로 성능 향상에 도움이 된다고 확인할 수 있다.

</br>

## Code

* Block 정의
```python
import torch
import torch.nn as nn
import torch.nn.functional as func
import torch.backends.cudnn as cudnn
import torch.optim as optim
import os

# 기본적인 Residual_Block 정의
class Residual_Block(nn.Module):
    def __init__(self, input, output, stride=1):
        super(Residual_Block, self).__init__()

        # 1번째 3x3 필터를 사용 (너비와 높이를 줄일 때는 stride 값 조절)
        self.conv1 = nn.Conv2d(input, output, kernel_size=3, stride=stride, padding=1, bias=False)
        self.bn1 = nn.BatchNorm2d(output) # 배치 정규화
        self.relu = nn.ReLU(inplace=True)

        # 2번째 3x3 필터를 사용
        self.conv2 = nn.Conv2d(output, output, kernel_size=3, stride=1, padding=1, bias=False)
        self.bn2 = nn.BatchNorm2d(output) # 배치 정규화

        self.shortcut = nn.Sequential() # identity인 경우 -> 아무런 변환을 수행하지 않고 입력을 그대로 전달하는 역할
        if stride != 1: # Identity mapping이 아닌 경우
            self.shortcut = nn.Sequential(
                nn.Conv2d(input, output, kernel_size=1, stride=stride, bias=False),
                nn.BatchNorm2d(output)
            )

    def forward(self, x):
      out = self.bn1(self.conv1(x))
      out = self.relu(out)
      out = self.bn2(self.conv2(out))
      out += self.shortcut(x) # skip connection
      out = self.relu(out)
      return out


# ResNet 클래스 정의
class ResNet(nn.Module):
    def __init__(self, block, num_blocks, num_classes=10):
        super(ResNet, self).__init__()
        self.in_planes = 64

        # 64개의 3x3 필터(filter)를 사용
        self.conv1 = nn.Conv2d(3, self.in_planes, kernel_size=3, stride=2, padding=1, bias=False)
        self.bn1 = nn.BatchNorm2d(64)
        self.relu = nn.ReLU(inplace=True)
        self.maxpool = nn.MaxPool2d(kernel_size=3, stride=2, padding=1)

        self.layer1 = self._make_layer(block, 64, num_blocks[0], stride=1)
        self.layer2 = self._make_layer(block, 128, num_blocks[1], stride=2)
        self.layer3 = self._make_layer(block, 256, num_blocks[2], stride=2)
        self.layer4 = self._make_layer(block, 512, num_blocks[3], stride=2)
        self.linear = nn.Linear(512, num_classes)

        self.avgpool = nn.AdaptiveAvgPool2d((1, 1))

    # 중간 블록 만들기.
    def _make_layer(self, block, planes, num_blocks, stride):
        strides = [stride] + [1] * (num_blocks - 1)
        layers = []
        for stride in strides:
            layers.append(block(self.in_planes, planes, stride))
            self.in_planes = planes # 다음 레이어를 위해 채널 수 변경
        return nn.Sequential(*layers)

    def forward(self, x):
        out = self.bn1(self.conv1(x))
        out = self.relu(out)
        out = self.maxpool(out)

        out = self.layer1(out)
        out = self.layer2(out)
        out = self.layer3(out)
        out = self.layer4(out)

        out =  self.avgpool(out)
        out = out.view(out.size(0), -1)
        out = self.linear(out)
        return out


# ResNet18 함수 정의
def ResNet18():
  return ResNet(Residual_Block, [2, 2, 2, 2])
def ResNet34():
  return ResNet(Residual_Block, [3, 4, 6, 3])
```

</br>

* 데이터 다운로드 및 설정
```python
import torchvision
import torchvision.transforms as transforms

transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    ])
train_dataset = torchvision.datasets.CIFAR10(root='./data', train=True, download=True, transform=transform)
test_dataset = torchvision.datasets.CIFAR10(root='./data', train=False, download=True, transform=transform)
print(train_dataset)
print(test_dataset)
train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=64, shuffle=True, num_workers=4)
test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=50, shuffle=False, num_workers=4)
```

* 결과  
<img src= "https://github.com/Sbeom12/study/blob/main/image/Resnet/%EC%BD%94%EB%93%9C%EA%B2%B0%EA%B3%BC1.JPG?raw=true" width='400' hegith = '100'>  


</br>

* 학습 환경 셋팅
```python
device = 'cuda'
l
model1 = ResNet18()
model1 = model1.to(device)
model1 = torch.nn.DataParallel(model1) # 데이터 병렬 처리
cudnn.benchmark = True # backpropagation 학습시 가장 적합한 알고리즘을 선정해 수행.

file_name = 'resnet18_cifar10.pt'

criterion = nn.CrossEntropyLoss()
optimizer = optim.AdamW(model1.parameters())
def train(epoch):
    print('[ Train epoch: %d ]' % epoch)
    model1.train()
    train_loss = 0
    correct = 0
    total = 0
    for batch_idx, (inputs, targets) in enumerate(train_loader):
        inputs, targets = inputs.to(device), targets.to(device)
        optimizer.zero_grad()
        outputs = model1(inputs)
        loss = criterion(outputs, targets)
        loss.backward()
        optimizer.step()
        train_loss += loss.item()
        _, predicted = outputs.max(1)

        total += targets.size(0)
        correct += predicted.eq(targets).sum().item()
    train_acc = 100. * correct / total
    train_loss /= total
    train_accu_list.append(train_acc)
    train_loss_list.append(train_loss)
    print('Total  train accuarcy:', train_acc)
    print('Total  train loss:', train_loss)


def test(epoch):
    print('[ Test epoch: %d ]' % epoch)
    model1.eval()
    test_loss = 0
    correct = 0
    total = 0

    for batch_idx, (inputs, targets) in enumerate(test_loader):
        inputs, targets = inputs.to(device), targets.to(device)
        total += targets.size(0)

        outputs = model1(inputs)
        test_loss += criterion(outputs, targets).item()

        _, predicted = outputs.max(1)
        correct += predicted.eq(targets).sum().item()

    test_acc = 100. * correct / total
    test_loss /= total
    test_accu_list.append(test_acc)
    test_loss_list.append(test_loss)
    print('Test accuarcy:', test_acc)
    print('Test average loss:', test_loss)


    state = {
        'model1': model1.state_dict()
    }
    if not os.path.isdir('checkpoint'):
        os.mkdir('checkpoint')
    torch.save(state, './checkpoint/' + file_name)
    print('Model Saved!')
```

</br>

* 학습 및 결과
```python
import matplotlib.pyplot as plt
train_accu_list = []
train_loss_list = []
test_accu_list = []
test_loss_list = []

for epoch in range(0, 20):
    train(epoch)
    test(epoch)

plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(train_accu_list, label='Train Accuracy')
plt.plot(test_accu_list, label='Test Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(train_loss_list, label='Train Loss')
plt.plot(test_loss_list, label='Test Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()

plt.show()
```

* ResNet18 결과  
<img src= "https://github.com/Sbeom12/study/blob/main/image/Resnet/%EC%BD%94%EB%93%9C%EA%B2%B0%EA%B3%BC2.JPG?raw=true" width='300' hegith = '100'>    
<img src= "https://github.com/Sbeom12/study/blob/main/image/Resnet/%EC%BD%94%EB%93%9C%EA%B2%B0%EA%B3%BC3.JPG?raw=true" width='600' hegith = '100'>  

* ResNet34 결과  
<img src= "https://github.com/Sbeom12/study/blob/main/image/Resnet/%EC%BD%94%EB%93%9C%EA%B2%B0%EA%B3%BC4.JPG?raw=true" width='300' hegith = '100'>    
<img src= "https://github.com/Sbeom12/study/blob/main/image/Resnet/%EC%BD%94%EB%93%9C%EA%B2%B0%EA%B3%BC5.JPG?raw=true" width='600' hegith = '100'>  


