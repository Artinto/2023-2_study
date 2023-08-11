def solution(progresses, speeds):
    answer = []
    days = 0 # 날짜 세기
    cnt = 0 # 완료된 기능
    while len(progresses) > 0:
    	# 기능의 진행상황과 그 동안 지난 날짜만큼의 speed를 구해서 더하기
        if(progresses[0]+days*speeds[0])>=100:
            # 완료되면 리스트에서 제거
            progresses.pop(0)
            speeds.pop(0)
            # 완료된 기능 수
            cnt += 1
        else:
        	# 만약 완료된 기능이 있다면 answer에 더해주고 0으로 초기화
            if cnt > 0:
                answer.append(cnt)
                cnt = 0
            # 완료된 기능이 없으면 days 추가
            else:
                days+=1
    answer.append(cnt)
    return answer
