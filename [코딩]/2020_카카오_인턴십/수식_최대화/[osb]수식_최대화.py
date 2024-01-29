import re
from itertools import permutations

def solution(expression):
    
    answers = []
    operators =re.findall('[^\d]+',expression) # 연산자 추출.
    set_operators = set(operators) # 순열 사용을 위해서 집합으로 선언
    nums = re.findall('\d+',expression) # 숫자 추출.
    cases = list(permutations(set_operators)) # 순열 계산.
    
    for case in cases:
        operators =re.findall('[^\d]+',expression) # 리스트 초기화
        nums = re.findall('\d+',expression)
        for operator in case: # 우선 순위대로 계산
            while operator in operators: # 계산식에 존재할때까지 반복.
                temp = 0
                idx = operators.index(operator) # 계산해야하는 위치 찾기
                oper = operators.pop(idx) # 계산후 연산자 제거
                num1, num2 = int(nums.pop(idx)), int(nums.pop(idx)) # 연산을 위한 숫자 추출.
                # 연산
                if oper == '*':
                    temp = num1 * num2
                elif oper == '+':
                    temp = num1 + num2
                else:
                    temp = num1 - num2
                nums.insert(idx, temp) # 원래 순서에 숫자를 넣어줌.
                
        answers.append(abs(nums[0])) # 최종값만 answers에 넣기
    return(max(answers))