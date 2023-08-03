def solution(phone_book):
    answer = True
    phone_book = sorted(phone_book)
    # ["119", "97674223", "1195524421"] string 형태이기 때문에 119, 1195524421, 97674223 순서로 정렬
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
        # 정렬되어 있기 때문에 접두어로 쓰이는 단어 바로 뒤에 접두사가 존재.
        # 슬라이싱을 통해 접두어의 길이만큼만 비교
            answer = False
    return answer
