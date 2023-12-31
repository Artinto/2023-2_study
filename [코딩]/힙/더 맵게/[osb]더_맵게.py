# -*- coding: utf-8 -*-
"""[OSB]더 맵게.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vXidQdHocCaNjx3QigCfObgFRN58Cv3T
"""

import heapq
def solution(scoville, K):
    answer = 0
    scov = 0
    heapq.heapify(scoville)
    while scoville[0] < K and len(scoville) > 1:
        scov = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville,scov)
        answer +=1
        if scoville[0] < K and len(scoville) == 1:
            answer= -1
            break
    return answer