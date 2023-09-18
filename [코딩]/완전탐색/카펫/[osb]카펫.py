def solution(brown, yellow):
    total_tile = brown+yellow
    answer = []
    for i in range(2, int(total_tile**0.5) + 1):
        if (total_tile%i) ==0:
            answer.append([i, total_tile//i])
    for x, y in answer:
        if (x-2) *(y-2) == yellow:
            if y >= x:
                answer = [y,x]
            else:
                answer = [x,y]
    return answer
