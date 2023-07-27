# 이전 완주하지 못한 선수 문제에서 다른 사람 풀이에서 collection모듈의 counter를 사용하여 요소를 비교하여 남은 요소를 배열로 불러와서 사용하는 것을 참고
# defaultdict는 딕셔너리의 기본값을 설정

from collections import defaultdict, Counter

def solution(genres, plays):
    genre_play_count = defaultdict(int)  # 각 장르별 노래 재생 횟수 누적 딕셔너리, 기본값 0
    song_play_count = defaultdict(list)  # 각 노래의 재생 횟수를 기억하는 딕셔너리, 기존에 있는 장르에 추가로 재생 횟수 추가

    # 각 노래의 장르와 재생 횟수를 순회하며 노래 재생 횟수 누적 합계 계산, 장르의 딕셔너리 값 저장
    for i, (genre, play) in enumerate(zip(genres, plays)): # enumerate로 zip을 이용하여 두 요소를 묶은 리스트와 i간의 요소와 인덱스관계를 반환
        genre_play_count[genre] += play # 각 장르별 노래 재생횟수 누적
        song_play_count[genre].append((i, play)) # 장르별 노래의 인덱스 i 와 노래 재생 횟수 play를 튜플로 저장

    # 장르별 재생 횟수 합계를 기준으로 장르 정렬
    sorted_genres = sorted(genre_play_count.keys(), key=lambda x: genre_play_count[x], reverse=True)
    # sorted 딕셔너리 키 정렬
    # lambda x: genre_play_count[x]로 정렬 기준 설정 : 장르별로 재생횟수를 비교하여 정렬
    # reverse=True 재생 횟수가 높은 것에서 낮은 것으로 정렬



    answer = []
    # 재생횟수 기준으로 정렬된 장르를 가져와 순회
    for genre in sorted_genres:
        # 각 장르 내에서 노래들을 재생 횟수가 많은 순으로 정렬하고 최대 2개까지만 선택하여 각 고유번호를 저장
        songs_in_genre = [song[0] for song in sorted(song_play_count[genre], key=lambda x: x[1], reverse=True)[:2]]
        answer.extend(songs_in_genre) # 저장된 고유번호를 extend를 사용하여 리스트answer에 리스트 songs_in_genre 리스트를 확장

    return answer
