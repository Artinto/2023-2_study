def solution(number, k):
    answer = ''
    while (k != 0): ## k : 버릴 수 있는 카드 수
        num = number[:k+1] ## 맨 앞 자리에는 [0]부터 [k+1]번째 카드만 올 수 있음
        n = '0'
        drop = 0 ## 이번에 버리게 될 카드 수
        for i in range(len(num)):
            if num[i] > n:
                n = num[i]
                drop = i
                if n == '9':
                    break
        k -= drop
        number = number[drop+1:]
        answer += n
        if k == len(number): ## 남은 숫자 카드 갯수가 k와 같을 경우
            k = 0
            number = ''
    return answer+number
