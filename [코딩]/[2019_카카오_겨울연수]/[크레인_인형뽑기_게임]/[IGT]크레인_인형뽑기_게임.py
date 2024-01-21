def solution(board, moves):
    board = [[bb for bb in b if bb] for b in zip(*board[::-1])]
    
    # [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]  >>  [[3, 4], [5, 2, 2], [1, 4, 5, 1], [3, 4], [1, 2, 1, 3]]
    
    busket = [0]
    answer = 0
    for m in moves:
        if board[m-1]:
            busket += [board[m-1].pop()]
            if busket[-1] == busket[-2]:
                del busket[-2:]
                answer += 2
    return answer
