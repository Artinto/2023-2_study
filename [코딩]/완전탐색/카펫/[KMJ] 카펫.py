# row = 3, col = 3
# while(row * col == total)
# row > col
# if row * col < total: col++
# if row < col: row++, col = 3

#####################################################
하나하나 다 비교하니까 시간초과

# def solution(brown, yellow):
#     answer = []
#     total = brown + yellow
#     row = 3
#     col = 3
#     while(row * col != total):
#         if row * col < total:
#             col += 1
#         if row <= col:
#             row += 1
#             col = 3        
#     answer.append(row)
#     answer.append(col)
#     return answer


######################################################

def solution(brown, yellow):
    answer = []
    total = brown + yellow
    
    for col in range(1,total+1):
        
        if (total / col) % 1 == 0: # 세로가 더 짧으므로 세로부터 비교
                                   # 전체 수에 세로가 나누어 떨어지면 카펫모양이 성립
            row = total / col
            
            if row >= col: # 조건1, 가로가 더 커야한다
                if 2 * row + 2 * col == brown + 4: # 조건2, 갈색의 개수가 맞아야한다 
                    answer.append(row)
                    answer.append(col)
    return(answer)
