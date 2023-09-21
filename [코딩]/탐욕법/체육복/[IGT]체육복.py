def solution(n, lost, reserve):
    lost = set(sorted(lost)) ## 체육복을 잃어버린 학생들의 집합(오름차순)
    reserve = set(reserve) ## 여벌 체육복을 갖고 있는 학생들의 집합
    exc = lost&reserve
    lost -= exc
    reserve -= exc
    for i in lost:
        if {i-1,i+1} & reserve != set(): ## 해당 학생의 앞뒷번호 학생이 여벌 체육복을 갖고 있는가?
            reserve.remove(min(list({i-1,i+1}&reserve))) ## 갖고 있다면 집합에서 제외(앞번호부터)
        else:
            n -= 1
    return n
