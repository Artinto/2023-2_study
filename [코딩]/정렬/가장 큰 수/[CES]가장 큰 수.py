def solution(numbers):
    answer = ''
    
    num = list(map(str, numbers))
    num = sorted(num, key = lambda x: x*3, reverse = True)
    
    return str(int(''.join(num)))
