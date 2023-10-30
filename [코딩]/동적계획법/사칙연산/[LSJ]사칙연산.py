def solution(arr):
    min_val, max_val = 0, 0  # 최소값과 최대값을 초기화합니다.
    sum_value = 0  # 합계를 초기화합니다.
    for idx in range(len(arr)-1, -1, -1):  # 주어진 배열을 역순으로 순회합니다.
        if arr[idx].isdigit():  # 숫자면
            sum_value += int(arr[idx]) # 합계에 더함
        elif arr[idx] == '+':  # '+' # continue
            continue
        elif arr[idx] == '-':  # '-' 연산자가 나오면
            temp_min, temp_max = min_val, max_val  # 현재까지의 최소값과 최대값을 임시 변수에 저장합니다.
            min_val = min(-(sum_value + temp_max), -sum_value + temp_min)  # 최소값을 업데이트합니다.
            minus_v = int(arr[idx+1])  # '-' 연산자 다음의 숫자를 가져옵니다.
            max_val = max(-(sum_value + temp_min), -minus_v + (sum_value - minus_v) + temp_max)  # 최대값을 업데이트합니다.
            sum_value = 0  # 합계를 초기화합니다.
    max_val += sum_value  # 마지막으로 합계를 최대값에 더합니다.
    return max_val  # 최대값을 반환합니다.
