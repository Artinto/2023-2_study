3from itertools import product # 중복순열

def solution(word):
    alphabets = ['A', 'E', 'I', 'O', "U"]
    results = []
    for r in range(1,6):
      for p in product(alphabets, repeat=r): # 1~5 길이의 중복순열 생성 후 반복문
        results.append(''.join(p)) #만들어진 순열들을 각각의 문자열로 변환
    results = list(set(results)) # 같은 순열들이 있을 수 있기에 ->집합->리스트
    results.sort() # 후 변경된 순서 재정렬
    answer = results.index(word)+1 # 원하는 단어의 위치
    return answer
