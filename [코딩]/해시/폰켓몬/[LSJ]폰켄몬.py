'''
중복이 있는 N마리의 폰켄몬 중 N//2마리의 폰켄몬을 뽑을 때 가능한 폰켄몬 종류의 수의 최대값은?
'''
def solution(nums):
    answer = 0 #없어도 됨
    type_num = len(set(nums)) # 보유중인 폰켄몬의 종류의 수
    select_num = len(nums)//2 # 뽑아야 하는 폰켄몬의 수
    if type_num > select_num:
        answer = select_num
    else:
        answer = type_num
    return answer
