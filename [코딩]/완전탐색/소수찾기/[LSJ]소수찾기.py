import math
from itertools import permutations 
# 소수 판단을 위한 함수
def is_prime(number):
    if number <= 1:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    else:
        sqrt_n = int(math.sqrt(number))
        for i in range(3, sqrt_n + 1, 2):
            if number % i == 0:
                return False
        return True

def solution(numbers):
    prime_numbers = set() # 만들어진 소수들을 넣을 집합
    for length in range(1, len(numbers) + 1): # 만들 숫자들의 길이
        permuts = list(permutations(numbers, length)) # 숫자 조합
        for permut in permuts:
            num_str = "".join(permut) # 만들어진 문자열을 정수형태로
            num_int = int(num_str)
            if is_prime(num_int): # 만들어진게 소수라면
                prime_numbers.add(num_int) # 집합에 추가
    answer = len(prime_numbers) # 집합의 길이 = 소수의 개수
    return answer
'''
permutations : 순열. permutations(arr, i) => arr 배열에서 i 개씩 조합해서 리스트로 만듦. ex) arr = [1,2] : ([1,2], [2,1])
'''
