def solution(routes):
    routes.sort(key=lambda x: x[1]) # 진출 지점 기준으로 정렬
    camera = -30001 # 카메라 위치 초기화
    answer = 0

    for route in routes:
        if camera < route[0]: # 현재 카메라 위치보다 뒤에 진입하는 차량이 있다면,
            answer += 1 # 새로운 카메라를 설치하고,
            camera = route[1] # 해당 차량의 진출 지점에 카메라를 설치합니다.

    return answer

