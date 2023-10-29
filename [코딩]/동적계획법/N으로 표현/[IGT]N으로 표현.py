def solution(N, number):
    num_list = [set([N])]
    n = 1
    while True:
        if number in num_list[n-1]: # number가 {5를 n번 사용해서 만들 수 있는 숫자들}에 들어있으면
            return n                # n을 return
        elif n == 8:                # 횟수가 8보다 커지면
            return -1               # -1을 return
        else:
            n += 1
            S = set()
            for i in range(n):          # n이 3이라면 N(5)을 3개 사용한다
                a = int(str(N)*(i+1))   # a = 5, 55, 555
                b = n - (i+1)           # b = 2, 1, 0
                if b:
                    for j in num_list[b-1]:  # a가 5라면 b는 2, list에서 index 1번에 있는 집합(5를 2번 사용하는 경우)를 꺼낸다
                        S.add(a+j)
                        S.add(a-j)
                        S.add(j-a)
                        S.add(a*j)
                        S.add(a//j)
                        S.add(j//a)
                else:
                    S.add(a)
            S.discard(0)  # {}안에 0이 있으면 제거, 없으면 pass
            num_list.append(S) # num_list 리스트에 집합 {5를 n번 사용해서 만들 수 있는 숫자들}를 n-1번째 index로 넣는다



""""
5를 이용해서 12를 만들려고 한다. 필요한 5의 갯수는 최소 몇 개인가?

1) 5를 1번 사용해서 만들 수 있는 숫자들의 집합 -> 5 -> num_list 리스트에 집합 {5}를 0번째 index로 넣는다
2) 5를 2번 사용해서 만들 수 있는 숫자들의 집합
ㄴ>  i) 5와 {5를 1번 사용해서 만들 수 있는 숫자들 (= 5)}과 만들 수 있는 숫자들의 집합 -> 5+5, 5-5, 5*5, 5//5 -> {10, 25, 1}
    ii) 55
3) 5를 3번 사용하는 경우, 만들 수 있는 숫자들의 집합
ㄴ>  i) 5와 {5를 2번 사용해서 만들 수 있는 숫자들 (= 55, 10, 25, 1)}과 만들 수 있는 숫자들의 집합
    ii) 55와 {5를 1번 사용해서 만들 수 있는 숫자들 (= 5)}과 만들 수 있는 숫자들의 집합
   iii) 555
.
.
.

""""

def solution(N, number):
    num_list = [set([N])]
    n = 1
    while True:
        if number in num_list[n-1]:
            return n
        elif n == 8:
            return -1
        else:
            n += 1
            S = set()
            for i in range(n):
                a = int(str(N)*(i+1))
                b = n - (i+1)
                if b:
                    for j in num_list[b-1]:
                        S.update([i for i in [a+j,a-j,j-a,a*j,a//j,j//a] if i]) # 0을 제외한 숫자들을 집합에 넣는다
                else:
                    S.add(a)
            num_list.append(S)
