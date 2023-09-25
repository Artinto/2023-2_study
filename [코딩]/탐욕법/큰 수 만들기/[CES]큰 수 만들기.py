def solution(number, k):
    answer = [] # Stack
    # 빈 리스트 answer를 스택으로 사용
    for num in number:
      # 문자열 number를 순회. 이때, num은 number의 각 숫자를 나타
        while k > 0 and answer and answer[-1] < num:
          # k가 0보다 크고, answer가 비어있지 않으며, answer의 가장 위에 있는 숫자(answer[-1])가 현재 숫자 num보다 작을 때까지 다음을 반복
            answer.pop()
          # 스택의 가장 위에 있는 숫자를 제거
            k -= 1
          # 제거한 숫자가 하나 늘어났으므로 k를 1 감소
        answer.append(num)
      # 현재 숫자 num을 스택에 추가
        
    return ''.join(answer[:len(answer) - k])
  # 택에 남아있는 숫자들을 문자열로 변환한 뒤, 맨 뒤에서 k개의 숫자를 제외한 나머지를 선택하여 반환
  # 이렇게 함으로써 최대 k개의 숫자를 제거하여 가장 큰 숫자를 만들 수 있게된다
