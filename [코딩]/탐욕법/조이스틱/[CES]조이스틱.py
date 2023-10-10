def solution(name):
    
    spell_move = 0
    # 알파벳 변경 횟수를 spell_move에 저장 (상하 이동)
    
    cursor_move = len(name) - 1  
    # 커서 이동 횟수를 cusor_move에 저장 (좌우 이동)
    
    for i, spell in enumerate(name):
        # index의 값이 필요하기 때문에 enumerate를 사용하여 인덱스를 값을 같이 for문에 돌린다
    	# 알파벳 변경 횟수, 위아래 중 최소 이동 값 ( 상하 이동 )
        
        spell_move += min(ord(spell) - ord('A'), ord('Z') - ord(spell) + 1)
        # ord함수 : 하나의 문자를 인자로 받고 해당 문자에 해당하는 유니코드 정수를 반환
        # 입력받은 spell의 유니코드 값과 A의 차이와 반대로 이동했을 때의 차이중에 더 작은 값을 spell_move에 저장        
        
        next = i + 1
        # 입력받은 알파벳 다음부터 연속된 문자열 A를 찾는다
        while next < len(name) and name[next] == 'A':
            next += 1
        # next 값보다 name의 길이가 더 크고 그 숫자가 A라면 next변수에 누적하여 1씩 더함
            
        # 아래 3가지 경우 중 최소 이동 값으로 갱신
        # 1. 이전 커서 이동 값 ( 초기값 - 이름의 길이 - 1 )
        # 2. 연속된 A의 왼쪽 시작
        # 3. 연속된 A의 오른쪽 시작
        cursor_move = min([ cursor_move, 2 * i + len(name) - next, i + 2 * (len(name) - next) ])
        # 앞에서 구한 cusor_move 값과 
        
    # 조이스틱 조작 횟수 = 알파벳 변경 횟수( 상하 이동 ) + 커서 이동 횟수( 좌우 이동 )    
    return spell_move + cursor_move
    # return spell 
