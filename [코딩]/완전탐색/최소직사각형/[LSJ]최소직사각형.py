def solution(sizes): # ex) [[60, 50], [30, 70], [60, 30], [80, 40]]
    width = max(max(size) for size in sizes) # (80, 70, 60, 60) => 80
    height = max(min(size) for size in sizes) # (50, 40, 30, 30) => 50
    answer = width * height # 4000
    return answer

'''
명함들은 다 돌릴 수 있기에 임의로 큰 쪽을 가로라 설정
가로 길이 중 가장 큰 값이 지갑의 가로 값
세로 길이 중 가장 큰 값이 지갑의 세로 값
위의 경우 모든 명함을 넣을 수 있는 지갑의 최소 넓이를 구할수 있음
'''
