def solution(genres, plays):
    answer = []
    dic={} # 같은 장르를 모아주는 딕셔너리
    for num in range(len(genres)):
        if genres[num] in dic: # dic에 "classic", "pop" 등의 장르가 있다면
            dic[genres[num]].append([plays[num],num]) # {"장르":[[재생횟수, 곡 번호], [재생횟수, 곡 번호]]}
            # print(dic)
        else : 
            dic[genres[num]] = [[plays[num],num]] # 새로운 장르 추가

    genre_rank ={}  # 장르별로 재생횟수를 정리하는 딕셔너리 {장르 : 총 재생횟수}
    for genre_name in dic.keys(): # dic.key는 dic 안에 있는 장르를 의미, "classic", "pop"
        plays_sum = 0 # 재생횟수 카운트 하는 변수
        # songs = dic[genre_name] # plays와 고유 횟수가 songs가 됨
        for song in dic[genre_name]: # plays와 고유 횟수가 songs가 됨
            plays_sum+=song[0] # song은 [plays, 고유 횟수] => song[0] == plays(재생 횟수)
            # 같은 장르의 재생횟수가 다 더해짐
        genre_rank[genre_name] = plays_sum # 딕셔너리 추가
    # print(genre_rank.items())
    genre_rank = sorted(genre_rank.items(), key=lambda x: x[1],reverse=True)
    # sort를 통해 재생횟수가 큰 순으로 정렬(reverse)
    # items()는 index와 key값을 모두 가져오겠다는 의미. (장르, 재생횟수)
    # key = lambda x:x[1]는 장르(0), 재생횟수(1) 중 재생횟수를 의미
    # 즉 재생횟수를 기준으로 sort를 진행
    
    for genre in genre_rank:
        # 이미 genre_rank는 정렬되어 있기 때문에 총 재생횟수가 많은 장르만 먼저 불러옴 => classic만 불러옴
        song_rank=sorted(dic[genre[0]], key=lambda x:-x[0])
        # sort를 통해 같은 장르 안에서 재생횟수가 많은 순서로 정렬
        # x:-x[0] = 재생 수를 기준으로 내림차순 (재생수가 많은 순으로 정렬)
        # reverse=True를 안쓰고 x:-x[0]으로도 쓸 수 있음
        
        best = 0 # 한 장르가 앨범에 3곡 저장되는 것을 방지
        for song in song_rank:
            answer.append(song[1]) 
            best +=1
            if best == 2:
                break

    return answer
