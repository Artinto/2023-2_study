# 효율성 테스트 통과 X

def solution(n, k, cmd):
    answer = ''
    cursor = k
    num = list(range(n)) # [0, 1, 2, 3, 4, 5] -> cursor : 3, C -> [0, 1, 2, 4, 5]
    delete = [] # 삭제된 3 추가 [3]
    result = ["O" for i in range(n)] # ["O", "O", "O", "X", "O", "O"]
    
    for s in cmd:
        if s[0] == "D":
            cursor += int(s[2:]) # 1의 자리 숫자가 아닐 수 있으므로 s[2]가 아니라 s[2:]
        elif s[0] == "U":
            cursor -= int(s[2:])
        elif s[0] == "C":   
            result[num[cursor]] = "X"
            if num[cursor] == num[-1]:
                cursor -=1
                delete.append(num.pop(cursor+1))
            else:
                delete.append(num.pop(cursor))
        elif s[0] == "Z":
            result[delete[-1]] = "O"
            if num[cursor] > delete[-1]:
                cursor += 1
            num.append(delete.pop())
            num.sort()
    answer = ''.join(map(str, result))
    return answer
