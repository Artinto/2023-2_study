def solution(s):
    answer = True
    stack = []
    for i in s:
        if i =='(':
            stack.append(i)
        elif i == ')':
            if stack:
                stack.pop()
            else: 
                return False
                break
    else :
        if not stack:
            answer = True
        else :
            answer = False
    return answer
