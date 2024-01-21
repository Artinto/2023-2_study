def solution(s):
    L = [set()] + [set(i.split(",")) for i in s[2:-2].split("},{")]
    # L = [set(), {'2'}, {'1', '2'}, {'1', '2', '3'}, {'1', '2', '3', '4'}]
    L.sort(key = lambda x:len(x))
    ans = [int((L[i]-L[i-1]).pop()) for i in range(1,len(L))]
    return ans
