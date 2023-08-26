def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1))) # enumerate로 리스트에 대해 인덱스 부여
    return answer

# 6 5 3 1 0 sorted
# 1 2 3 4 5 min
# 1 2 3 1 0 
# 3 max
