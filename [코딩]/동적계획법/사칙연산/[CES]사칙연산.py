def solution(arr):
    minmax = [0, 0]
    # minmax라는 길이가 2인 리스트 초기화 -> 최소값과 최대값 저장할 공간
    sum_value = 0
    # 현재까지의 합을 저장하는 변수를 0으로 초기화
    for idx in range(len(arr)-1, -1, -1):
    # 입력 리스트 arr를 뒤에서부터 앞으로 순회하는 루프 시작
        if arr[idx] == '+':
        # 현재 위치의 문자가 +이면 아무 동작도 하지 않고 다음 턴으로 넘어감
            continue
        elif arr[idx] == '-':
        # 현재 위치의 문자가 -이면, 최소값과 최대값을 갱신한다
            tempmin, tempmax = minmax
            # 변수에 현재의 최소값과 최대값을 복사
            minmax[0] = min(-(sum_value + tempmax), -sum_value+tempmin)
            # 최소값은 현재까지의 합에 이전 최대값을 더한 것과 현재까지의 합에서 이전 최소값을 빼는 것 중 더 작은 값을 선택 -> -가 이전 값에 붙는 경우와 전체 수식에 붙는 경우를 고려
            minus_v = int(arr[idx+1])
            # 현재 위치의 다음 문자를 정수로 변환하여 변수에 저장
            minmax[1] = max(-(sum_value+tempmin), -minus_v+(sum_value-minus_v)+tempmax)
            # 최대값은 현재까지의 합에 이전 최소값을 더한 것과 현재까지의 합에서 현재 위치의 숫자를 뺀 후 이전 최대값을 더한 것 중 더 큰 값을 선택한다 -> -가 현재 값에 붙는 경우와 다음 값에만 붙는 경우를 고려
     
            sum_value = 0
            # 현재까지의 합을 0으로 초기화
        elif int(arr[idx]) >= 0:
        # 현재 위치의 문다가 +나 -가 아니고 양의 정수인 경우
            sum_value += int(arr[idx])
            # 현재 값을 sum_value에 더한다
    minmax[1] += sum_value
    # 마지막으로 남은 sum_value를 최대값 minmax[1]에 더한다
    return minmax[1]
    # 최대값은 minmax[1]을 반환 -> 주어진 수식을 평가하여 얻은 최대값을 나타낸다
