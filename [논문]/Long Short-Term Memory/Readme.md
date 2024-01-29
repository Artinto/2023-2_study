# LONG SHORT-TERM MEMORY(1997)
## Abstract
* 당시 Vanilla RNN은 Time Interval이 큰 데이터에 대한 정보를 잘 저장하지 못하는 한계점이 존재했고 이 문제를 해결하기 위해 LSTM을 제안
* 본문에서는 인위적으로 만들어낸 다양한 패턴들에 대해서 LSTM을 적용시켜 실험하여 우수함을 입증
* 단순한 성능 지표만 높을 뿐 아니라, 기존 RNN류 모델들이 풀지 못했던 Long Time Lag Task에서 최초로 성공을 거둠

## Introduction
* Real-Word 시계열데이터(Time-Series Data)에서 우수한 성능을 보임
* 기존 Vanilla RNN은 모델이 깊어지면서 생기는 수많은 time step으로 인한 layer층들로 인해 vanishing gradient현상이 발생하게 되는데 이는 RNN의 Activation function이 tanh라는 점이 point(Back Propagation Through Time:BPTT)

## Previous work
### 기존 RNN구조
* 문제 : Long time step에 대해 학습이 제대로 되지 않음
* 원인 : Vanishing Gradient & Exploding Gradient
  * BPTT

    - Time Step이 무수하게 많은 경우, 행렬곱 $W_h$ 의 반복으로 인해 $W_h$ 값의 특이값에 따라 1보다 작으면 Vanishing, 1보다 크면 Exploding됨
    - Activation function인 tanh을 미분했을 경우, 1보다 작기 때문에 Vanising될 확률이 높음
   
<img src="https://ifh.cc/g/vyQFJr.jpg" width="300" height="270"/>   <img src="https://ifh.cc/g/JyBxRM.jpg" width="300" height="270"/>

* 문제를 해결하기 위한 시도
 * Gradient-descent variants -> 학습 방법의 다양성을 부여, BPTT와 동일한 기울기 소실 문제
 * Time_delays -> shor time에만 동작
 * Time_constant -> LSTM과 유사한 time constant를 사용했으나 fine tuning등이 필요
 * Bengio et algorithm approaches -> 특정 문제에 state가 너무 많이 필요

## Long Short-Term Memory
* 하나의 Step에서 계산된 Short-Term을 길게 전파하는 Memory구조를 제안
* 기존의 RNN Step보다 Vanishing/Exploding Gradient를 막으며, Long Time-Step 학습을 가능케 함

### Contribution
1. 장기기억 Cell 구조 도입 - Vanishing Gradient를 막음
   * 장기기억 Cell인 CEC(Constant Error Carousel)을 도입
   * Identity Mapping으로 Matrix변환 없이 정보를 다음 Step으로 전달
     
<img src="https://ifh.cc/g/GAMhMD.jpg" width="400" height="270"/>

<img src="https://ifh.cc/g/ASYZK5.jpg" width="360" height="270"/>   <img src="https://ifh.cc/g/pjZkwV.jpg" width="360" height="270"/>

2. Gate 구조의 도입 - 자동으로 input, output값에 대한 제어
   * Input Gate
     * 현재의 input과 이전 step의 output을 가져와 연산을 통해 Cell State를 업데이트하며 이때의 비율은 sigmoid를 통해 자동 결정
     * $i_t = \sigma(W_i\cdot[h_{t-1}, X_t]+bias) $
     * $S_t = squash(W_c\cdot[h_{t-1}, X_t]+bias)$
  
<img src="https://ifh.cc/g/ay9oCc.jpg" width="400" height="270"/>

   * Output Gate
     * 자동으로 Input, Output값에 대한 제어(Original LSTM에는 Forget Gate가 없음)
     * Cell State에서 다음 외부 Output이 될 $h_t$를 결정, 이때 비율은 sigmoid를 통해 자동 결정
     * $O_t = \sigma(W_o\cdot[h_{t-1}, X_t]+bias)$
     * $h_t = O_t\cdot squash(C_t)$
    
<img src="https://ifh.cc/g/3GcTYr.jpg" width="440" height="270"/>

   * Forget Gate
     * Highway Network(2015)의 Gate 구조를 도입하여 데이터를 얼마나 변환해서 보내줄지를 결정하는데서 Cell State가 1.0Weight만 주다보니 Deep할 수록 Exploding Gradient가 됨
     * 이 문제를 해결하기 위해 후속 논문으로 Froget Gate를 추가함
     * $f_t = \sigma(W_f \cdot[h_{t-1}, X_t]+bias)$

<img src="https://ifh.cc/g/7zZ7CX.jpg" width="360" height="270"/>   <img src="https://ifh.cc/g/5D8Gxp.jpg" width="360" height="270"/>

3. Training Method 개선 - BPTT와 RTRL(Real-Time Recurrent Learning)의 Variation을 동시에 학습 사용
   * BPTT - Output units, Hidden units, Output gates
     * 속도가 빠르며 일반적으로 사용하지만 Backward연산이 다로 필요하며 Vanishing Gradient가 잘 나타남
   * RTRL - Input gates, Cell(CEC)
     * 속도는 느리지만 BPTT보다 Vanishing Gradient에 강하고 Forward 연산 시 미분하여 Weight를 업데이트 하므로 따로 Training Phase가 필요없음

<img src="https://ifh.cc/g/zr1gQ6.jpg" width="400" height="270"/>

### Current Vanilla LSTM
* 학습 알고리즘은 Fully BPTT를 사용
* 현재 구조는 약 1,000step까지 학습 가능하다고 함

<img src="https://ifh.cc/g/CZnok7.jpg" width="600" height="270"/>

## Experiment

### Embedded Reber grammar

<img src="https://ifh.cc/g/JfnTaF.png" width="600" height="270"/>

* Shor Time Dataset에서도 잘 동작
* Output Gate만 사용해도 좋은 결과를 보여줌

### Noise-free and Noisy Sequence(100steps)

<img src="https://ifh.cc/g/3DvN6n.png" width="600" height="270"/>

* Noise가 없는 상황에서의 Sequence Classification Task
* RTRL은 10step만 되어도 학습이 안되는 반면, LSTM은 100step에서도 학습이 잘 되고 있음

## Conclusion

* RNN구조에 Cell State(CEC)라는 Identity Mapping으로 긴 Step의 Time_Series Data에서 Gradient를 안정적으로 학습할 수 있는 구조를 제안하였고, 후에 Deep Learning 연구에 많은 영향을 미침















