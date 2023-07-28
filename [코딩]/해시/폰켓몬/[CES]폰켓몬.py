def solution(nums):
    answer = 0
    
    num_len = len(set(nums))
    result = int(len(nums)/2)
    
    if result < num_len :
        answer = result
    else :
        answer = num_len
    
    return answer
