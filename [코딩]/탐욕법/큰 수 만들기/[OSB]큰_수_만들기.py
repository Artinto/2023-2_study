def solution(number, k):
    answer = []
    for num in number:
        if len(answer) == 0:
            answer.append(num)
            continue
        elif k>0:
            while len(answer) and answer[-1] < num and k>0:
                answer.pop()
                k-=1
        answer.append(num)
    # 12번 테스트 문제 4321순으로 작아지는 순이면 마지막을 지워야함.
    if k >0:
        answer = answer[:-k] # 뒤에서부터 k개지움.
    answer = ''.join(answer)
    return answer
