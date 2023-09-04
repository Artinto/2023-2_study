from itertools import permutations

def solution(numbers):
    def is_prime(n):
        if n < 2: # 만약 n이 2보다 작다면, 그 수는 소수가 아니므로 False를 반환
            return False
        for i in range(2, int(n**0.5) + 1): # 만약 n이 소수라면, 그 약수는 sqrt(n) 이하에 존재하므로 이 범위에서 반복
            if n % i == 0: # 만약 i가 n의 약수라면 (즉, n을 i로 나눴을 때 나머지가 없다면), 그 수는 소수가 아니므로 False를 반환
                return False
        return True

    nums = set()
    for r in range(1, len(numbers)+1):
        perms = permutations(list(numbers), r) # numbers 문자열에서 r개의 원소를 뽑아 순열(permutations)을 생성합니다.
        for perm in perms: 
            num = int(''.join(perm))
            nums.add(num)

    count = 0
    for num in nums:
        if is_prime(num):
            count += 1
            
    return count
