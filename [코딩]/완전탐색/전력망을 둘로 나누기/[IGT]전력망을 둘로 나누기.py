def solution(n, wires):
    answer = n-2 ## answer의 최대값
    for i in wires: ## i = [1,3]
        wire_connect = set([i[0]]) ## wire_connect = {1}
        cut_wire = wires[:]
        cut_wire.remove(i)
        ## cut_wire = [[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
        ## cut_wire는 끊어진 전선을 기준으로 생성된 두 개의 전력망의 구조를 나타냄
        set_len = 0 ## wire_connect에 변화가 있는지를 판단하는 변수
        while (set_len != len(wire_connect)):
            set_len = len(wire_connect)
            for j in cut_wire: ## j = [2,3]
                if (wire_connect & set(j)):
                ## 끊어진 전선의 한쪽 송전탑(1번)과 연결된 다른 전선이 있는가?
                    wire_connect = wire_connect | set(j)
        ## wire_connect : 1번 송전탑에 연결되어 있는 모든 송전탑들의 집합
        answer = min(answer, abs(n-2*len(wire_connect)))
        ## 두 전력망의 송전탑 차이 : (n-len(wire_connect) - len(wire_connect)
    return answer
