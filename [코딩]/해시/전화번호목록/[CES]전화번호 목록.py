def solution(phone_book):
    phone_book.sort()
    # sort를 통해 접두어가 있는 번호끼리 붙어있을 수 있도록 정렬
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
          # startswitch함수를 통해 뒤의 문자와 앞의 문자가 같은지 판별
            return False
          # if문을 만족한다면 접두어이기 때문에 False 출력
    return True
  # 그게 아니라면 True 출력
