def solution(prices):
    answer = []  

    # prices의 모든 원소를 순회하며 가격이 떨어지지 않은 기간을 계산
    for i in range(len(prices)):
        duration = 0  # 가격이 떨어지지 않은 기간을 저장할 변수 초기화

        # 현재 시점 이후의 원소들과 비교
        for j in range(i + 1, len(prices)):
            duration += 1  # 가격이 떨어지지 않은 시간을 1초씩 증가시킴

            # 현재 시점의 가격이 이후 시점의 가격보다 높다면, 가격이 떨어졌다고 판단
            if prices[i] > prices[j]:
                break  # 더 이상 비교할 필요가 없으므로 반복문 종료

        # 가격이 떨어지지 않은 기간을 answer 배열에 추가
        answer.append(duration)

    return answer  
