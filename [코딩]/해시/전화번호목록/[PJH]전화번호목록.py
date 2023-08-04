def solution(phone_book):
    phone_book.sort()  # 번호를 사전식 순서로 정렬
    
    # 인접한 두 번호를 비교하여 접두어인지 확인
    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False  # 하나의 번호가 다른 번호의 접두어인 경우 False를 반환
    
    return True  # 모든 번호를 확인한 후에도 접두어가 없는 경우 True를 반환

# startswith()는 파이썬 문자열 메서드로 주어진 문자열이 특정 접두사로 시작하는지 확인
# ex) string.wtartswith(prefix)에서 string은 검사하고자 하는 문자열, prefix는 접두사
