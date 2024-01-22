def solution(board, moves):
    count = 0
    answer = []
    
    for move in moves: # 옮길 열 선택
        for line in board: # 옮길 행 선택
            if line[move-1] != 0: # 행이 0이면 인형이 없는 것
                answer.append(line[move-1]) # 해당 행에 있는 인형을 정답 리스트에 추가
                line[move-1] = 0 # 인형을 옮겼으므로 0으로 변경
                break

        if len(answer) >= 2 and answer[-1] == answer[-2]: # 뒤에 있는 인형 2개가 같다 (삭제할 수 있다)
            count += 2 # 2개가 만나 삭제 됐으므로 2 카운트
            answer = answer[:-2] # 만난 인형들 삭제
            
    return count
