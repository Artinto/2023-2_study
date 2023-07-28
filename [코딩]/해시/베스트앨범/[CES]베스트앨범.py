def solution(genres, plays):
    answer = []
    total={} #장르별 총 재생횟수
    gen_dic={} #장르별 
    
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        if genres[i] in total.keys():
            total[genres[i]]+=plays[i]
            gen_dic[genres[i]].append((plays[i],i))
        else:
            total[genres[i]]=plays[i]
            gen_dic[genre]=[(play,i)]

        
    total = sorted(total.items(), key=lambda x: x[1], reverse=True)
    
    #print(total)
    #print(gen_dic)
    
    for key in total:
        playlist = gen_dic[key[0]]
        playlist = sorted(playlist, key=lambda x: x[0], reverse=True)
        for i in range(len(playlist)):
            if i==2:
                break
            answer.append(playlist[i][1])
            
        #print(playlist)
    return answer
