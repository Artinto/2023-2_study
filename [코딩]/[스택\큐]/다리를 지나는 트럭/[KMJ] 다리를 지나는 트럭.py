# bridge_length 길이만큼 0으로 채워진 bridge라는 list 생성
# truck_weights를 비울 때 까지 bridge에 값 추가
# truck_weights가 비워지면 모든 트럭이 다리를 지났거나 건너는 중
# 마지막 트럭이 다 지나갈때까지 시간이 경과해야 하므로 현재 answer에 bridge_lengh만큼 더하기

# bridge 맨 앞의 값 꺼내기(강 도착), 맨 뒤에 값 추가(대신 조건 존재) -> answer 1 증가

# 추가되는 값의 조건
# bridge 안에 있는 값들과 다음에 넣을 truck_weight[0]의 합이 weight보다 크면 bridge 뒤에 0 추가
# 아니라면 truck_weight[0] 추가

def solution(bridge_length, weight, truck_weights):
    answer = 0
    in_bridge = 0 # 다리 위 합
    
    bridge = [0] * (bridge_length-1)
    
    while truck_weights:
        in_bridge = 0 # 다리 위 합을 구하기 위해 초기화
        for num in bridge: # 다리 위 합 구하기
            in_bridge += num

        if in_bridge + truck_weights[0] > weight: # 대기 트럭이 올라올 수 없으면
            bridge.append(int(0)) # 뒤에 0 추가
        else: # 대기 트럭이 올라올 수 있으면
            bridge.append(truck_weights.pop(0)) # 뒤에 다음 대기 트럭 추가
                 
        bridge.pop(0) # 강을 건넜으므로 bridge 가장 앞에 있는 수 삭제
        answer += 1

    answer+=bridge_length
    return answer
