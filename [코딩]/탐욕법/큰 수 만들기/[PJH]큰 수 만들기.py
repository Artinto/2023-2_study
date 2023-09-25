def solution(number, k):
    stack = []
    for num in number:
        while stack and k > 0 and stack[-1] < num:
            k -= 1
            stack.pop()
        stack.append(num)
        
    if k != 0: # 모든 숫자를 처리한 후, 아직 제거해야 할 숫자가 남아있다면 (즉, k > 0), 스택에서 마지막 k개의 요소를 제거
        stack = stack[:-k]
        
    return ''.join(stack)
