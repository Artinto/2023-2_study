def solution(s):
    s=s[1:-1]
    s=s.split("},")
    # 이렇게 되면 앞의 { 이 부분만 남은 채 분리
    for i in range(len(s)):
        if i==((len(s))-1):
            s[i]=(s[i])[1:-1]
        else:
            s[i]=(s[i])[1:]
    s=sorted(s, key=lambda x:len(x))
    rs=[]
    for i in s:
        a=i.split(',')
        for j in a:
            if int(j) not in rs:
                print(j)
                rs.append(int(j))
    return rs
