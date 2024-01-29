import re

def solution(s):
    answer = []
    # 초기 정규화
    s = re.sub('{', '',s)
    s = re.sub('}}', '',s)
    s = s.split('},')
    s = sorted(s, key = lambda x : len(x)) # 무조건 낮은거 우선으로 들어오게됨.
    for datas in s:
        data = datas.split(',')
        for num in data:
            num=int(num)
            if num not in answer: # 없으면 넣고 있으면 안넣기
                answer.append(num)
    return answer