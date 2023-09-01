from functools import cmp_to_key 
def solution(numbers):
    compare = lambda a, b : -1 if a+b > b+a else 1 # 정렬이 오름차순임을 이용해서 
    nums = sorted([str(num) for num in numbers], key=cmp_to_key(compare)) # 조건에 맞게 정렬
    if nums[0] == '0': #모든 문자열이
        return '0' #0인 경우
    answer = ''.join(nums) # 하나의 문자열로 합침
    return answer

'''
cmp_to_key : 조건부 정렬 라이브러리
cmp : compare
'''
