def solution(routes):
    answer = 0
    # 모니터링에 필요한 최소 카메라 수를 저장
    routes.sort(key=lambda x: x[1]) 
    # routes 리스트를 경로의 끝 지점 (x[1])을 기준으로 오름차순으로 정렬
    # 끝 지점이 작은 경로를 우선적으로 처리하기 위해
    camera = -30001 
    # camera 변수를 경로의 시작 지점 중 가능한 가장 작은 값으로 초기화
    for route in routes:
    # routes 리스트를 반복문으로 순회
        if camera < route[0]:
        # 현재 camera 위치가 경로의 시작 지점 (route[0])보다 작은지 확인
        # 그렇다면 현재 경로가 camera로 커버되지 않았다는 뜻이므로 새로운 카메라를 설치해야함
            answer += 1
            # answer 변수를 1 증가시켜서 새로운 카메라 설치 표시
            camera = route[1]
            # camera 변수를 현재 경로의 끝 지점 (route[1])으로 업데이트
            
    return answer
    # answer 값 반환
