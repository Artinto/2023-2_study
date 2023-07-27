def solution(nums):
    n = len(nums) // 2
    unique_nums = len(set(nums))  # 폰켓몬 종류 번호의 개수 계산
    # set을 이용하여 폰켓몬의 중복된 값을 제거하여 정렬 후, len으로 그 개수 계산

    # n과 unique_nums 중 작은 값이 선택 가능한 폰켓몬 종류의 최댓값
    return min(n, unique_nums)

    # 만약 가져가야 하는 폰켓몬 수n에 비해 폰켓몬의 종류 수unique_nums가 작다면 n이 경우의 수가 되고
    # 만약 가져가야 하는 unique_nums에 비해 n이 작다면 unique_nums가 경우의 수가 되기 때문에 min을 이용한다.
