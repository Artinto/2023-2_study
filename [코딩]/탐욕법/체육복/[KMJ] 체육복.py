def solution(n, lost, reserve):
    answer = 0
    real_reserve = set(reserve) - set(lost)
    real_lost = set(lost) - set(reserve)
    
    for i in real_reserve:
        if (i - 1) in real_lost:
            real_lost.remove(i - 1)
        elif (i + 1) in real_lost:
            real_lost.remove(i + 1)
    answer += n - len(real_lost)
            
    return answer
