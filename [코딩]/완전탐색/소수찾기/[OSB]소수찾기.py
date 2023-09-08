from itertools import permutations
def solution(numbers):
    num_list= list(numbers)
    lennumber = len(numbers)
    total_list = []
    for i in range(1, lennumber+1):
        total_list +=list(permutations(num_list, i))
    for idx, permu in enumerate(total_list):
        temp = ''
        for i in permu:
            temp += i
        total_list[idx] = int(temp)
    total_list = list(set(total_list)) # 중복 제거
    answer = 0
    for i in total_list:
        if Prime(i):
            answer += 1
    return answer 


def Prime(num):
    if num <= 1:
        return False
    else:
        for v in range(2, int(num**0.5) +1):
            if (num % v) == 0:
                return False
        return True
