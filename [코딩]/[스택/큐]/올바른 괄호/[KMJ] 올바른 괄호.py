def solution(s):
    count = 0
    for i in s: # s
        if count < 0: # 처음에 ')'가 나오거나 '('보다 ')'가 많은 경우
            return False # False 반환
        if i == '(': # '('가 나오면
            count += 1 # count값 증가
        else: # ')'가 나오면
            count -= 1 # count값 감소
        
    if count != 0: # for문을 다 돌고난 뒤 count가 0이 아니면 올바르지 않은 괄호
        return False
    else: # count가 0이 나오면 올바른 괄호
        return True
    
