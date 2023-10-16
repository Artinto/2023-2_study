def solution(triangle):
    answer = 0
    for i in range(len(triangle)-2,-1,-1): # 역순으로 진행
        for j in range(len(triangle[i])): # i번째 줄의 수 개수
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1]) # i번째 줄의 수의 대각선 아래에 있는 i+1번째 줄 수들 중 큰 값 더함
            answer = triangle[0][0] # 큰 값들을 더하고 더했을 때 첫번째 줄까지 더한 값
    return answer
  '''
  위에서부터 내려가면 시작점부터 마지막 숫자들까지 각 경우의 수를 다 더한 후 비교해야하는데
  이 때 지나갔던 곳들을 또 지나가 중복되는 계산이 많아짐
  하지만 밑에서부터 계산을 한다면 중복으로 계산하지 않고 한번만 지나가면서도 최대값을 구할 수 있음
  '''
