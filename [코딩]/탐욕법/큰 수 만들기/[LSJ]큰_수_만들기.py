def solution(number, k):
    answer=''
    numbers = [] # 가장 큰 수를 만들 수들의 리스트
    for num in number: # number 안의 숫자들을 반복문 돌리는 동안
        while numbers and k > 0 and numbers[-1] < num: #numbers 비워x, k>0, 검사중인 숫자가 numbers 맨뒤보다 클 때
            k -= 1 # 제거해야 되는 숫자 카운트 -1
            numbers.pop() # 맨 뒤에 숫자 제거
        numbers.append(num) # numbers에 num 추가
    # [5,6] 일 때 num이 6보다 크면 [5]
    if k != 0:
        numbers = numbers[:-k] #역순 배열
    answer = ''.join(numbers) # 문자열 변환
    return answer
