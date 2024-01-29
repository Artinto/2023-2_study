from collections import deque
def solution(bridge_length, weight, truck_weights):
    # 각각의 변수를 입력받아 solution 함수에 대입
    time = 0
    # 걸린 시간을 나타내는 time 변수 0 으로 초기화
    bridge = deque([0] * bridge_length)
    # 초기에 다리 위에 아무것도 없는 상태를 나타내기 위해 0을 길이만큼 반복하여 초기화
    truck_weights = deque(truck_weights)
    # 아직 다리에 올라가지 않은 트럭들의 부게 정보를 담은 큐
    currentWeight = 0
    # 현재 다리 위에 올라간 트럭들의 무게합을 나타내는 변수 0 으로 초기화
    while len(truck_weights)!=0:
        time+=1
# 아직 다리 위에 올라가지 않은 트럭이 있을 때까지 무한 루프 반복
# 시간은 1씩 누적하여 더함
        currentWeight -= bridge.popleft()
# 현재 다리의 맨 앞에 있는 트럭을 다리에서 뺌
        if currentWeight + truck_weights[0] <= weight:
        # 다리 위 트럭들의 무게 합과 다음으로 올라갈 트럭의 무게를 비교하여 최대 무게 초과하지 않는 경우만 if문 실행
            currentWeight+= truck_weights[0]
            # 다음 트럭의 무게를 currentWeight에 추가하고 bridge에 해당 트럭을 추가한다
            bridge.append(truck_weights.popleft())
# 추가한 트럭은 truck_weights 큐에서 제거
        else: 
            bridge.append(0)
            # 최대 무게 초과할 경우 현재 시간에 트럭대신 무게 0을 bridge에 추가 (-> 대기하는 시간 적용)
    time += bridge_length
    # 마지막 트럭이 다리를 건너는 동안에도 다리의 길이만큼 시간이 추가로 걸린다 -> time변수에 bridge_length를 더해줌
    return time
# 앞의 코드를 통해 전체 걸린 time을 return 해줌
