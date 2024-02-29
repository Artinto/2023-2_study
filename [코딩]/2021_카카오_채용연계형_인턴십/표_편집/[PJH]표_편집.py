def solution(n, k, cmd):
    # 초기 테이블 설정
    cur = k
    table = {i: [i - 1, i + 1] for i in range(n)}
    table[0][0], table[n - 1][1] = None, None

    # 초기 상태 설정
    answer = ['O'] * n
    stack = []

    for c in cmd:
        if c == "C":
            # 현재 행 삭제
            answer[cur] = 'X'
            prev, nxt = table[cur]
            stack.append((prev, cur, nxt))
            if prev is not None:
                table[prev][1] = nxt
            if nxt is not None:
                table[nxt][0] = prev
            del table[cur]  # 테이블에서 현재 행 제거
            cur = nxt if nxt is not None else prev  # 다음 행 또는 이전 행 선택
        elif c == "Z":
            # 가장 최근에 삭제된 행 복구
            prev, now, nxt = stack.pop()
            answer[now] = 'O'
            if prev is not None:
                table[prev][1] = now
            if nxt is not None:
                table[nxt][0] = now
            table[now] = [prev, nxt]  # 테이블에 복구된 행 추가
        else:
            # 커서 이동
            direction, distance = c.split()
            distance = int(distance)
            for _ in range(distance):
                cur = table[cur][0 if direction == 'U' else 1]  # 위 또는 아래로 이동
                
    return ''.join(answer)  # 결과 반환
