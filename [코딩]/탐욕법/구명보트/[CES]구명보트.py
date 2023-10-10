def solution(people, limit) :
# solution 함수 정의
    answer = 0
    # ansewer을 0으로 정의
    people.sort()
    # sort함수를 이용해서 사람들의 몸무게를 오름차순으로 정의 (가벼운 순)

    a = 0
    # a를 0으로 초기화
    # 가벼운 사람
    b = len(people) - 1
    # people의 값을 끝에서부터 살펴보기 위해 b에 그에 맞는 index값 저장
    # 무거운 사람
    while a < b :
    # b가 a보다 크다면 반복문 실행
        if people[b] + people[a] <= limit :
        # 양 끝 값을 더해서 그 값이 limit보다 작거나 같다면
            a += 1
            # a에 누적하여 1을 더해준다
            answer += 1
            # answer에 누적하여 1을 더해준다
        b -= 1
        # 반복문이 한번 실행될 때마다 b값을 1씩 감소시켜준다
    return len(people) - answer
    # 2명이 한 보트로 처리되는 경우를 고려해야하기 때문에 이러한 return값을 사용
