import re
from itertools import permutations

def solution(expression):
    # 연산자만 따로 추출
    operations = [x for x in ['*', '+', '-'] if x in expression]
    # 연산자를 기준으로 숫자를 분리
    numbers = re.split('\D', expression)
    # 가능한 모든 연산자 우선순위 조합
    operation_permutations = permutations(operations)
    
    max_result = 0
    for ops in operation_permutations:
        temp_numbers = numbers.copy()  # 수식에서 숫자 부분만 복사
        temp_operations = re.findall('\D', expression)  # 수식에서 연산자 부분만 추출
        for op in ops:
            while op in temp_operations:
                idx = temp_operations.index(op)  # 해당 연산자의 인덱스를 찾음
                # 해당 연산자와 양 옆의 숫자를 함께 계산
                temp_numbers[idx] = str(eval(temp_numbers[idx] + op + temp_numbers[idx + 1]))
                # 계산에 사용된 숫자와 연산자를 제거
                del temp_numbers[idx + 1]
                del temp_operations[idx]
        # 계산된 결과의 절댓값이 이전 결과보다 크다면 업데이트
        max_result = max(max_result, abs(int(temp_numbers[0])))

        
    return max_result
