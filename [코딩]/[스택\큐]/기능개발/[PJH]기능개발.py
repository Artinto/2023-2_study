def solution(progresses, speeds):
    answer = []  # 현재 배포의 기능 개수를 저장할 리스트 초기화
    days = [0] * len(progresses)  # 각 작업이 완료되는데 필요한 일수를 저장할 리스트 초기화

    for i in range(len(progresses)):
        remaining = 100 - progresses[i]  # 남은 작업 진도 계산
        days[i] = -(-remaining // speeds[i])  # 남은 작업일 계산(올림을 하기 위해 음수에 나누어 자동 내림 진행 후 -로 다시 반전)

    while days:
        count = 0  # 배포되는 기능의 수 초기화
        current_day = days.pop(0)  # 현재 작업일을 삭제하고 반환
        count += 1  # 첫 번째 기능 카운트 추가

        # 남아있는 작업들 중 작업일이 같거나 작은 것들을 카운트하고 삭제
        while days and days[0] <= current_day:
            days.pop(0)
            count += 1

        # 현재 배포 기능 개수 저장
        answer.append(count)

    return answer  # 배포 기능 개수 리스트 반환
