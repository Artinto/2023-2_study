def solution(phone_book):
    answer = True
    phone_book.sort() # 문자열 순서대로 정렬
    for i in range(len(phone_book)-1): #문자열 개수 만큼 반복
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]: # ex) ["123", "1234", ...] 일 때 "1234" 중 "123"의 길이만큼만 잘라서 비교
            answer = False # 뒤에 요소 안에 앞의 요소가 있으면
            break
    return answer
