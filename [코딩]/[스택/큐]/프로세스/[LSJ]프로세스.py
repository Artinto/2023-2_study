def solution(priorities, location):
    queue = [(i, p) for i, p in enumerate(priorities)] # priorities의 값들을 인덱스와 요소로 구분
    answer = 0
    while queue: # queue 값들이 남아있다면
        max_priority = max(queue, key=lambda x: x[1]) # p값이 가장 큰 값
        cur_index, cur_priority = queue.pop(0) # queue의 첫 번째 값이 
        if cur_priority == max_priority[1]: # 최대값이라면
            answer += 1 # answer 값 + 1 => 맨 처음엔 0->1
            if cur_index == location: # 해당 요소의 인덱스가 문제에서 주어진 location 값이라면
                break # 종료
        else: # 최대값이 아니라면
            queue.append((cur_index, cur_priority)) # queue의 맨 뒤로 옮김
    return answer
