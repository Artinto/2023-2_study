def solution(board, moves):
    basket = [] 
    c = 0 
    for m in moves:
        for i in range(len(board)):
            if board[i][m-1] != 0:
                print(board[i][m-1])
                basket.append(board[i][m-1])
                board[i][m-1] = 0
                break  
        
        if len(basket) > 1 and basket[-2] == basket[-1]:
            basket.pop()
            basket.pop()
            c += 2
                
    return c
