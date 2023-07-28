from collections import Counter #Collection 모듈 중 Counter 클래스 사
def solution(participant, completion):
    participant_counts = Counter(participant) #Counter로 요소 별 개수 파악. ex) a:1, b:2, c:1
    completion_counts = Counter(completion)
    
    difference = list((participant_counts - completion_counts).elements())[0] #차이 요소를 리스트화 시킨 후 첫 번 째 요소
    return difference
'''
def solution(participant, completion):
  for item in completion:
    if item in participant:
      participant.remove(item)
  return participant[0] 
'''
