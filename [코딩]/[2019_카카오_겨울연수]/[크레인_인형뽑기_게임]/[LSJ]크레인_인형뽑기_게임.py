def solution(board, moves):
  basket = []
  answer = 0  # 제거된 인형의 개수

  for move in moves:
      j = move - 1  # 0부터 시작하는 인덱스로 변환

      # 해당 열에서 인형을 뽑음
      for i in range(len(board)):
          if board[i][j] != 0:  # 인형이 있는 경우
              doll = board[i][j]
              board[i][j] = 0  # 해당 칸을 0으로 변경

              if basket and basket[-1] == doll:  # 바구니의 top과 현재 인형이 같은 경우
                  basket.pop()  # 바구니의 top을 제거
                  answer += 2  # 제거된 인형의 개수 증가
              else:
                  basket.append(doll)  # 바구니에 인형 추가
              break # 사실 얘는 없을 때 생기는 문제를 생각하지 못 하겠음

  return answer
'''
의문점 : j =  move-1로 반복문마다 변환하는 것보다 인덱스에서 변환하는것이 더 효율적이라는데 코드를 돌려본 결과 위 쪽의 코드가 더 빠름. 왜?
def solution(board, moves):
  basket = []
  answer = 0  # 제거된 인형의 개수

  for j in moves:
      # 해당 열에서 인형을 뽑음
      for i in range(len(board)):
          if board[i][j-1] != 0:  # 인형이 있는 경우
              doll = board[i][j-1]
              board[i][j-1] = 0  # 해당 칸을 0으로 변경

              if basket and basket[-1] == doll:  # 바구니의 top과 현재 인형이 같은 경우
                  basket.pop()  # 바구니의 top을 제거
                  answer += 2  # 제거된 인형의 개수 증가
              else:
                  basket.append(doll)  # 바구니에 인형 추가
              break

  return answer
'''
