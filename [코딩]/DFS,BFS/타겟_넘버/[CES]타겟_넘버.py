def solution(numbers, target):
    answer = 0
    # answer을 0으로 초기화
    def dfs(idx, total):
        nonlocal answer 
        # 비지역 변수 선언
        if idx == len(numbers):
        # numbers의 index 값 만큼 if문을 다 돌았을 때
            if total == target: 
            # total이 target 값과 같다면
                answer += 1
                # answer에 누적하여 1씩 더해준다
        else:
            dfs(idx + 1, total + numbers[idx]) 
            # 재귀호출 선언 -> +1을 곱한 경우
            dfs(idx + 1, total - numbers[idx]) 
            # 재귀호출 선언 -> 요소에 -1를 곱한 경우
    dfs(0,0)
    # 함수 시작 코드
    return answer
