def solution(genres, plays):
    answer = [] # # 결과를 담을 리스트 초기화
    total={} #장르별 총 재생횟수를 담을 딕셔너리 초기화
    gen_dic={} #장르별 곡의 (재생횟수, 인덱스) 정보를 담을 딕셔너리 초기화
    
    for i in range(len(genres)): # 장르별 총 재생횟수 계산과 곡 정보 저장
        genre = genres[i]
        play = plays[i]
        # 만약 해당 장르가 total 딕셔너리에 이미 존재하면 재생횟수를 더해주고, 곡 정보를 gen_dic에 추가
        if genres[i] in total.keys():
            total[genres[i]]+=plays[i]
            gen_dic[genres[i]].append((plays[i],i))
        else: # # 해당 장르가 처음 나오는 경우 딕셔너리에 추가
            total[genres[i]]=plays[i]
            gen_dic[genre]=[(play,i)]

        # 장르별 총 재생횟수를 기준으로 내림차순으로 정렬
    total = sorted(total.items(), key=lambda x: x[1], reverse=True)
    # 장르별 곡의 재생횟수를 기준으로 내림차순으로 정렬하고, 최대 2곡까지 answer 리스트에 추가
    for key in total:
        playlist = gen_dic[key[0]]
        playlist = sorted(playlist, key=lambda x: x[0], reverse=True)
        for i in range(len(playlist)):
            if i==2:
                # 최대 2곡만 answer에 추가
                break
            answer.append(playlist[i][1])
    return answer
