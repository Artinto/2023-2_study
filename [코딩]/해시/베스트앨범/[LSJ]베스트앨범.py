from collections import defaultdict
# defauldict : 유사 딕셔너리. 값을 지정하지 않은 키는 자동으로 값이 디폴트 값으로 지정됨
def solution(genres, plays):
'''
genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
'''
    answer = []
    song_dict = {i: (genre, int(play_count)) for i, (genre, play_count) in enumerate(zip(genres, plays))}
    # enumerate와 zip 통해 {고유번호 i,(genres, plays)}로 이루어진 딕셔너리 생성
  
    genre_play_count = defaultdict(int) #유사 딕셔너리 생성, 디폴트 값이 int=>0 만약 int 자리에 list? => []이 디폴트 값
    for _, (genre, play_count) in song_dict.items(): #.items() 통해 {i : (genres, plays)}를 (i,(genres,plays))로 인식
        genre_play_count[genre] += play_count #각 장르에 해당하는 키의 값에 각 노래의 재생횟수 더함
      
    sorted_genres = sorted(genre_play_count.items(), key=lambda x: x[1], reverse=True) # 0:pop, 1:classic
    # lambda : 익명함수? 매개변수를 이용하는 함수 x=> (genre, playcount), x[1] => playcount
  
    for genre, _ in sorted_genres: 
        songs = sorted([(i, cnt) for i, (g, cnt) in song_dict.items() if g == genre], key=lambda x: x[1], reverse=True)
    '''
    song_dict.items()
    (0, ('classic', 500)),
    (1, ('pop', 600)),
    (2, ('classic', 150)),
    (3, ('classic', 800)),
    (4, ('pop', 2500))
    '''
        songs_to_add = songs[:2] #각 장르의 두번째 요소까지만 묶음
        answer.extend([i for i, _ in songs_to_add])  #(i,(genre,plays))에서 i 부분만 추가
    return answer
