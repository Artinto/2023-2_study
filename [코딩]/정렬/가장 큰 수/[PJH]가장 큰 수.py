def solution(numbers):
    numbers = list(map(str, numbers))

    # 사용자 지정 비교 함수
    numbers.sort(key=lambda x: x*3, reverse=True)
    # 문자열로 비교하여 각 인자의 맨 앞자리 수를 비교
    # x*3로 인자를 3번 반복하는 이유는 제한 사항이 1000이하로 4자리 숫자 이하이기 때문

    # 리스트의 모든 문자열을 연결
    answer = ''.join(numbers)
    
    return str(int(answer))  # 앞부분에 '0'들이 오면 '0' 하나만 남기고 삭제
