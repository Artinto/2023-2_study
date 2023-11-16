# Focal Loss for Dense Object Detection(RetinaNet)

## Object Detection
![image](https://github.com/Artinto/2023-2_study/assets/84369594/1583d22b-ae9a-48d7-8a5a-781e56814c10)
![image](https://github.com/Artinto/2023-2_study/assets/84369594/bbc8a8ec-8899-46ce-84b6-155cf648ed4c)
![image](https://github.com/Artinto/2023-2_study/assets/84369594/aadf3b52-14b5-4a46-8014-e7236da89e38)
![image](https://github.com/Artinto/2023-2_study/assets/84369594/f806ed47-e31c-4f57-a1ce-39cf49f61fad)

## Focal Loss

+ cross entropy loss

$y$ : object일 때는 1, background일 때는 0

$p$ : $y = 1$ 일 probability

$$CE(p,y) = 
\begin{cases}
-log(p), & \mbox{if }y = 1 \\
-log(1-p), & otherwise
\end{cases}$$




$$CE(Foreground) = −log(0.95) = 0.05$$

$$CE(Background) = −log(1 - 0.05) = 0.05$$


+ balanced cross entropy loss

$$CE(p,t) = −\omega_t \ log(p_t)$$

+ Focal Loss

$$FL(p_t) = −\alpha_t \ (1-p_t)^\gamma \ log(p_t)$$

![image](https://github.com/Artinto/2023-2_study/assets/84369594/31e0af09-d0ba-46b9-86ec-3caae14b8a6d)

![image](https://github.com/Artinto/2023-2_study/assets/84369594/dd78075b-bd7c-4fe8-b648-18c4637ece99)


## FPN(Feature Pyramid Network)
![image](https://github.com/Artinto/2023-2_study/assets/84369594/8df352ec-9583-4662-b194-6fa98c90b00e)

