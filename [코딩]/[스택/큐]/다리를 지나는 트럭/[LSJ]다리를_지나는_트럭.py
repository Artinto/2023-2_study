def solution(bridge_length, weight, truck_weights):
    answer = 0
    passing_truck = [0]* bridge_length # | 0 ,, 0| 현재 다리 위에 있는 트럭 현황. |0,7|이면 7짜리 트럭 하나만 다리 위에 있음
    while passing_truck: # 다리 위에 트럭이 있는 동안(대기 중인 트럭이 있는 동안)
      answer += 1 # while이 진행되는 동안 = 트럭이 지나가고 있는 동안 매 초 카운트
      passing_truck.pop(0) # 트럭이 다리 위에 새로 추가 되므로 다리 길이 값을 유지하기 위해 맨 앞의 0 제

      if truck_weights: # 트럭이 다 지나갈 때까지
        if sum(passing_truck) + truck_weights[0] <= weight: #이미 지나가고 있던 트럭과 새로 추가될 트럭의 무게의 합이 weight보다 크지 않다면
          t = truck_weights.pop(0) 
          passing_truck.append(t) # 다리에 해당 트럭 추가
        else:
          passing_truck.append(0) # 아니라면 다리 길이 유지하기 위해 0 추가
        
    return answer # 트럭이 완전히 다 지나갔다면 종료, 값 반환
