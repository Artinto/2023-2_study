# 순열을 만들어주는 모듈
from intertools import permutations

# 소수 판별 함수
def is_prime_number(x):
    if x < 2:
      # x가 2보다 작다면
        return False
      # 소수가 아님 = False
    for i in range(2,x):
      # 2부터 x-1까지 반복
        if x % i == 0:
          # 나머지가 0이 나온다면
            return False
          # 소수가 아님 = False
    return True
  # 위의 두 조건을 만족하지 않는다면 소수 = True

# 순열 모듈을 사용해서 나올 수 있는 모든 수 조합
def solution(numbers):
    answer = 0
    num = []
    for i in range(1, len(numbers)+1):
      # 1부터 numbers의 개수까지 반복
        num.append(list(set(map(''.join, permutations(numbers, i)))))
      # permutations 모듈을 사용하여 순열 생성
    per = list(set(map(int, set(sum(num, [])))))
  # 앞에서 만든 순열을 합쳐주고 그것을 per에 저장
    for p in per:
        if is_prime_number(p) == True:
            answer += 1
    return answer
