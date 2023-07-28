def solution(nums):
    answer = len(set(nums)) # 중복된 종류를 제거한 포켓몬 수
    move = len(nums) // 2 # 가져갈 수 있는 포켓몬 수
    if move > answer:
        return answer
    else:
        return move
