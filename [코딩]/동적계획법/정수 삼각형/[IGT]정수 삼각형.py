def solution(triangle):
    a = []
    for i in reversed(triangle):
        while(a): # a = [] (False)
            for k in range(len(i)):
                i[k] += a[k]
            a = []
        for j in range(len(i)-1):
            a.append(max(i[j], i[j+1]))
        if not a:
            return i[0]

"""
          7
        3  8
      8  1  0
    2  7  4  4
  4  5  2  6  5

숫자들을 거쳐가면서 나온 결과값이 최대가 되기 위한 방법은 다음과 같다.
제일 아랫줄에 있는 숫자는 4, 5, 2, 6, 5
그 윗줄에 있는 숫자는 2, 7, 4, 4
임의의 경로를 통해 숫자들을 지나가였고 그 결과가 최대라고 가정하자.
그 과정에서 4번째 줄에 있는 숫자 2를 거쳤다면, 그 다음은 반드시 숫자 5를 거쳐야 한다(max(4,5)).
마찬가지로 4번째 줄에 있는 숫자 7을 거쳤다면, 그 다음은 반드시 숫자 5를 거쳐야 한다(max(5,2)).
4번째 줄에 있는 숫자 4를 거쳤다면, 그 다음은 반드시 숫자 6을 거쳐야 한다(max(2,6)).
정리하면, 4번째 줄에 있는 각각의 숫자들 [2, 7, 4, 4]는 [5, 5, 6, 6]의 기댓값을 갖는다고 말할 수 있다.
이를 더하면 [7, 12, 10, 10]이 되는데, 4번째 줄에 있는 4개의 숫자들을 이로 치환하고, 마지막 줄에 있는 숫자들을 지워도 결과는 동일해진다.
위 과정을 계속 반복하여 한 줄 한 줄 지워나가면, 결국 최대의 결과값을 얻을 수 있다.

[5, 5, 6, 6]
[12, 12, 10]
[20, 13]
[23]
[]
"""

def solution(triangle):
    for i in range(len(triangle)-2, -1, -1):
        for j in range(len(triangle[i])):
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])
    return(triangle[0][0])
