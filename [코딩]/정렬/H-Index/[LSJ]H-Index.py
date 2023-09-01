def solution(citations):
    citations.sort(reverse = True) # [6 ,5 ,3 , 1, 0]
    for i, citation in enumerate(citations): # [[0,6], [1,5], [2,3], [3,1], [4,0]]
        if i >= citation: # h번 이상 인용된 논문의 수가 h 이상인 경우
            return i
    return len(citations) # 반복문이 끝까지 진행됐는데도 답이 안 나온 경우: 모든 논문이 0회 이상 인용됐으므로 H-index = len(citation)
    # ex) [10, 9, 8, 7, 6] => [[0,10], [1,9], [2,8], [3,7], [4,6] => 논문 수인 5가 답. 5번 이상 인용된 논문의 수가 5개.
