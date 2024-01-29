def solution(bridge_length, weight, truck_weights):
    queue = [0] * bridge_length  # 다리 길이만큼 0으로 채운 초기 queue 생성
    count = 0
    total_weight = 0

    while truck_weights:  # 대기 트럭이 남아있는 동안 반복
        count += 1
        total_weight -= queue.pop(0)  # 다리를 빠져나가는 트럭의 무게를 제거

        if total_weight + truck_weights[0] <= weight:  # 트럭이 다리 위에 올라올 수 있는지 확인
            truck = truck_weights.pop(0)  # 대기 중인 첫 번째 트럭을 다리에 올림
            queue.append(truck)  # 새로운 트럭의 무게를 추가
            total_weight += truck  # 현재 다리 위의 총 트럭 무게를 업데이트
        else:
            queue.append(0)  # 아닌 경우, 0을 추가하여 시간 경과

    answer = count + bridge_length # 트럭이 완전히 다리를 건너는데 필요한 추가 시간 포함
    return answer
