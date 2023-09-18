def solution(brown, yellow):
    s = brown + yellow
    x = 3 ## x : 가로 길이의 최소값
    while (s/x != (yellow/(x-2))+2): ## y=s/x로 구한 y가 (x-2)*(y-2)=yellow를 만족할 때까지
        x += 1
    return sorted([x, int(s/x)], reverse=True)
