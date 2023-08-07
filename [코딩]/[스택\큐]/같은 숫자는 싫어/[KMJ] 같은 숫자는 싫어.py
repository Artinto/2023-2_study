def solution(arr):
    answer = [] # 연속된 수를 제거한 값들을 넣을 리스트 생성
    answer.append(arr[0]) # 비교할 필요 없는 첫번째 수는 answer에 추가
    for i in range(1,len(arr)):
        if arr[i] == arr[i-1]: # 앞의 수와 동일하면
            pass # 리스트에 추가하지 않고 패스
        else:
            answer.append(arr[i]) # 동일하지 않으면 추가
    return answer
