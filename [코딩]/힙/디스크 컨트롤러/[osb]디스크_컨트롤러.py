# -*- coding: utf-8 -*-
"""[OSB]디스크 컨트롤러.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GFxwwiClX9l59s37e9zVkLXoEf6J62Zd
"""

import heapq
def solution(jobs):
    answer = 0
    time = 0 # 시간
    length = len(jobs)
    jobs.sort() # 요청 시간으로 정렬.
    heap = []
    while len(jobs) != 0 or len(heap) != 0:
        while len(jobs) != 0 and time >= jobs[0][0] : # 현재 시점에서 작업이 가능한 경우.
            temp = jobs.pop(0)
            heapq.heappush(heap, (temp[1], temp[0]))
        if len(heap)  == 0: # 대기목록에 없는 경우
            time = jobs[0][0] # 작업할 수 있느 시점으로 이동.
            continue
        # 디스크 작업 종료
        temp = heapq.heappop(heap)
        time += temp[0] # 맨압 뺴오기
        answer += time - temp[1]
    answer = answer // length
    return answer