# Focal Loss for Dense Object Detection(RetinaNet)

## Object Detection
![image](https://github.com/Artinto/2023-2_study/assets/84369594/1583d22b-ae9a-48d7-8a5a-781e56814c10)
![image](https://github.com/Artinto/2023-2_study/assets/84369594/bbc8a8ec-8899-46ce-84b6-155cf648ed4c)
![image](https://github.com/Artinto/2023-2_study/assets/84369594/aadf3b52-14b5-4a46-8014-e7236da89e38)
![image](https://github.com/Artinto/2023-2_study/assets/84369594/f806ed47-e31c-4f57-a1ce-39cf49f61fad)

## Focal Loss

![image](https://github.com/Artinto/2023-2_study/assets/84369594/93aa18cd-c4d7-454a-8eec-c6a13d2691e8)

+ cross entropy loss

$y$ : object일 때는 1, background일 때는 0

$p$ : $y = 1$ 일 probability, $p \in [0,1]$

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

![image](https://github.com/Artinto/2023-2_study/assets/84369594/dc9b202a-4897-4cf1-a21c-deb1e6e5b968)

![image](https://github.com/Artinto/2023-2_study/assets/84369594/2163bc87-e635-4a3a-b856-f6b265c18681)

## FPN(Feature Pyramid Network)
![image](https://github.com/Artinto/2023-2_study/assets/84369594/8df352ec-9583-4662-b194-6fa98c90b00e)

![image](https://github.com/Artinto/2023-2_study/assets/84369594/7c632b73-5f10-41fb-9187-3ed740d9092c)



+ output featuremaps of FPN

![image](https://github.com/Artinto/2023-2_study/assets/84369594/c001c713-def8-4890-a1f3-a40cede0af72)


![image](https://github.com/Artinto/2023-2_study/assets/84369594/1eb66a2d-eb09-4b22-a3a4-b63d89ae8e46)

## Experiments

+ Focal loss

![image](https://github.com/Artinto/2023-2_study/assets/84369594/45e59010-df17-4802-a386-009429b20dae)


![image](https://github.com/Artinto/2023-2_study/assets/84369594/91df2792-7a58-450c-a64b-49ac8f7cac05)

+ Comparison to State of the Art

![image](https://github.com/Artinto/2023-2_study/assets/84369594/bdf6cd50-7846-4d42-9f01-2c361e57e797)
