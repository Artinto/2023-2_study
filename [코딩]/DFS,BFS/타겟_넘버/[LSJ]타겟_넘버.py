def solution(numbers, target):
    answer = 0
    def dfs(idx, total):
        nonlocal answer # 비지역 변수를 불러옴
        if idx == len(numbers): # numbers 내 요소들을 다 돌았을 때
            if total == target: # + 또는 -를 가해 합산한 값이 target과 같다면
                answer += 1 # 경우의 수 + 1
        else: # 아직 numbers 내 요소를 도는 중이라면
            dfs(idx + 1, total + numbers[idx]) # 재귀호출. 요소에 +1를 곱한 경우
            dfs(idx + 1, total - numbers[idx]) # 재귀호출. 요소에 -1를 곱한 경우
    dfs(0,0) # 함수의 시작. (0,0) -> (len(numbers),@)까지 진행
    return answer
'''
비지역 변수란? 
함수가 중첩되어 있는 상황에서 외부 함수의 변수는 내부 함수 기준에선 비지역 함수이므로 내부 함수에서 외부함수의 변수를 쓰려면
nonlocal 키워드를 붙여 사용

global과의 차이점?
global은 전역 변수를 활용할 때 쓰는 키워드로 중첩된 함수의 변수가 아닌, 함수의 외부에 있는 변수를 함수 내부에서 사용할때 쓰임
