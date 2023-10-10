def solution(name):
    answer = 0
    min_side_moves = len(name) - 1 # 기본 최소 좌우 이동 횟수는 길이 - 1
    for idx, char in enumerate(name): 
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1) # 해당 알파벳 변경 최솟값 추가
        next_char_idx = idx + 1
        while next_char_idx < len(name) and name[next_char_idx] == 'A': # 해당 알파벳 다음부터 연속된 'A' 문자열 찾기
            next_char_idx += 1 
        min_side_moves = min([min_side_moves, 2 * idx + len(name) - next_char_idx, idx + 2 * (len(name) - next_char_idx)]) # 기존, 연속된 'A'의 왼쪽 시작 방식, 연속된 'A'의 오른쪽 시작 방식 비교 및 갱신
    answer += min_side_moves # 알파벳 변경(상하 이동) 횟수에 좌우 이동 횟수 추가
    return answer
  # 초기 상태 : AAA
  # ord : 주어진 문자에 대한 유니코드 코드 포인트. ex) ord('A') = 65, ord('Z') = 90
