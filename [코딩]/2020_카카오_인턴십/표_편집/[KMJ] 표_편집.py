# 틀린 코드

def solution(n, k, cmd):
    answer = ''
    curser = k
    num = list(range(n))
    delete = []
    result = ["O" for i in range(n)]
    
    for s in cmd:
        if s[0] == "D":
            curser += int(s[2:])
        elif s[0] == "U":
            curser -= int(s[2:])
        elif s[0] == "C":
            result[num[curser]] = "X"
            delete.append(num.pop(curser))
        elif s[0] == "Z":
            result[delete[-1]] = "O"
            if num[curser] < delete[-1]:
                curser -= 1
            else:
                curser += 1
            num.append(delete.pop())
            num.sort()
    answer = ''.join(map(str, result))
    return answer
