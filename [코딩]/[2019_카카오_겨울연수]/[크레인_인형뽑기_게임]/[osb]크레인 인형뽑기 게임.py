from collections import deque
def solution(board, moves):
    moves = deque(moves)
    out = deque() # 인형 뽑기 결과.
    answer = 0
    while moves:
        move = moves.popleft() # 어디로갈지 하나 빼기
        for line in board:
            if line[move-1] == 0:
                continue
            out.append(line[move-1]) # 인형뽑기로 뺀거 추가.
            line[move-1] = 0 
            break
        if len(out) > 1 and out[-1] == out[-2]: # 뒤에서 첫번째랑 두번쨰가 같다면
            answer += 2
            out.pop()
            out.pop()
        
    return answer