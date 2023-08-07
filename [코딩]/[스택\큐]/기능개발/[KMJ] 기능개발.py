# progresses에 speeds만큼 더하기
# 만약 progresses[0]이 100이 되면 100보다 작은 값이 나올 때까지 progresses, speeds값 pop & 몇개 pop했는지 count
# answer에 count값 추가 후 초기화
# progresses가 비워질 때까지 반복

def solution(progresses, speeds):
    answer = [] # 정답을 넣을 리스트 생성
    count = 0
    
    while progresses: # progresses list가 비워지면 반복 종료
        if progresses[0] < 100: # 배포가 불가능한 상황
            
            if count != 0: # count 초기화
                answer.append(count)
                count = 0           
            else: # for문을 한번 돌 때마다 하루가 지남
                for i in range(len(progresses)):
                    progresses[i] += speeds[i]
        else: # 배포가 가능한 상황
            progresses.pop(0) and speeds.pop(0) # 앞에서부터 100이 된 만큼 pop으로 제거하고
            count += 1 # count 증가
            
    answer.append(count) # progresses가 비워지면 마지막 배포 가능한 count 추가
    return answer
