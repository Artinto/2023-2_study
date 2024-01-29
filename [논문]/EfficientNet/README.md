# EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks(2019)

## Abstract
+ Network의 깊이(Depth), 폭(Width), 해상도(Resolution)이 균형을 이룰 때 보다 더 좋은 성능을 보인다는 것을 확인했다
+ 모든 차원에서 깊이, 폭, 해상도를 균일하게 scaling하는 새로운 방법을 제안하려고 한다

## Introduction
![image1](https://github.com/Artinto/2023-2_study/assets/84369594/a1cba886-47de-4804-b586-9415fbca58e4)
+ 다른 Model들은 Parameter 수가 많을 수록 정확도가 올라가는 양상을 보이지만, EfficienNet의 경우 더 적은 Parameter로 높은 Accuracy를 보인다는 것을 확인할 수 있다

![image2](https://github.com/Artinto/2023-2_study/assets/84369594/913e5a09-52e9-48d4-8b31-82db1c2eba87)
+ Convolution Network의 scale-up은 정확도를 높이기 위해 사용된다
+ Convolution Network의 scale-up 방법에는 대표적으로 3가지가 있다.
  + Network의 Depth를 늘리는 것(=layer의 갯수 증가) : 가장 흔한 방법, ex) ResNet-200
  + Channel Width를 늘리는 것(=filter의 갯수 증가) : Width를 넓게 할 수록 미세한 정보들이 많이 담긴다고 한다
  + Input Image의 Resolution을 늘리는 것(=해상도 향상) : 더 큰 Size의 Image를 넣었을 때 성능이 올라간 것을 실험으로 확인하였다

+ 대부분은 1가지 차원에 대해서만 scaling 하였는데, 2차원 이상으로 scaling을 할 경우 많은 수동 조정이 필요할 뿐더러 정확성과 효율성이 떨어지는 경우가 많다


## Related work
+ ConvNet Accuracy
  + Convolution Network의 정확도는 나날이 높아지고 있지만 그와 함꼐 model의 size도 같이 커져 나갔다
  + Hardware Memory Limit 이슈로 Model Size를 늘리는 것이 아닌 효율성에 초점을 맞춰야 한다

+ ConvNet Efficiency
  + 효율성을 높이기 위한 방법 중 하나로 Modeling Compression이 있는데, 모델 크기를 줄여 효율성을 높일 수 있지만 정확도가 낮아지게 된다
  + 또한 설계 공간이 크고 튜닝 비용이 비싼 대형 Model의 경우 이러한 방식을 적용하기 어렵다
  + 큰 모델에서도 효율성을 높일 수 있는 방법이 필요하다

+ Model Scaling
  + Depth, Width, Resolution을 모두 효율적으로 조절하는 방법이 필요하다

## Compound Model Scaling

![image3](https://github.com/Artinto/2023-2_study/assets/84369594/73f73ec1-0d25-469e-92ac-81f6b07cb655)

FLOP : FLoating point OPerations, 딥러닝 모델이 얼마나 빠르게 동작하는지(초당 연산량)를 계산하는 지표

+ width scaling : 그러나 극단적으로 넓지만 얕은 모델은 더 높은 수준의 특징을 포착하기 어려움

+ depth scaling : 깊은 신경망은 더 좋은 성능을 달성 할 수 있으나 신경망을 계속 깊게 쌓는 것은 한계가 있다 ex)vanishing gradient
  + 실제로 ResNet-1000 과  ResNet-101 은 거의 비슷한 성능을 가진다

+ 더 좋은 정확도와 효율성을 얻기 위한 scaling 방법은?


![image4](https://github.com/Artinto/2023-2_study/assets/84369594/bd3180d3-5cf0-4663-8887-34be691e53e8)


+ Network의 Depth, Width, Resolution 전부를 균형있게 조정하는 것으로 더 높은 정확도와 효율성을 얻을 수 있다는 것을 알아냈다
+ 이를 바탕으로 본 논문에서는 효과적인 scaling 기법이라 할 수 있는 Compound Scaling Method를 제안한다



##  EfficientNet Architectur

![image5](https://github.com/Artinto/2023-2_study/assets/84369594/1b9dcdc1-544a-4b8d-b63a-8e5ab28a95ba)
![image](https://github.com/Artinto/2023-2_study/assets/84369594/8bd5f60e-7143-46d5-a07c-d747c0eaea59)
![image](https://github.com/Artinto/2023-2_study/assets/84369594/a41448d3-924f-4943-80eb-668513708aa3)
![image](https://github.com/Artinto/2023-2_study/assets/84369594/324be5e5-49f7-40c2-bf9d-3f80de4bbd8d)
![image](https://github.com/Artinto/2023-2_study/assets/84369594/01dc5589-fb17-4ea2-9f66-9497769b139e)



+ Baseline Model 구축

![image6](https://github.com/Artinto/2023-2_study/assets/84369594/bfbed986-ab91-4f56-a5e3-6a536c459c6b)



## Experiments


![image7](https://github.com/Artinto/2023-2_study/assets/84369594/8f37c425-3880-40a6-9c4e-06b6ba15a4ac)

![image8](https://github.com/Artinto/2023-2_study/assets/84369594/ebb267e9-9b8a-4e69-9ac3-1bb36a2939c6)

+ 기존 Model들에 비해 훨씬 낮은 연산량임에도 뛰어난 성능을 보여주고 있다
+ EfficientNet이 Parameter 수가 적어 FLOPS도 작게 나타나지만 Accuracy는 월등히 높은것을 확인할 수 있다.

![image9](https://github.com/Artinto/2023-2_study/assets/84369594/a8191eae-abff-488f-bea9-435a0372f1b1)

+ 기존 Convolution Model보다 Parameter 수는 최대 8배 차이나거나 FLOPS가 최대 19배까지도 차이나지만 추론속도는 약 6배정도 빨라졌다. 속도 향상에도 긍정적인 효과가 있음을 알 수 있다.

## Discussion



![image13](https://github.com/Artinto/2023-2_study/assets/84369594/2f250ddf-c6b8-4525-88a3-5a16d781d30a)



![image14](https://github.com/Artinto/2023-2_study/assets/84369594/a4d908c8-7b85-47a9-8cd8-cd9459a15b45)



![image15](https://github.com/Artinto/2023-2_study/assets/84369594/d172cd95-f4dd-46b5-9b70-d091ed269a28)
