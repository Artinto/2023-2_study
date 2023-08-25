def solution(operations):
    answer = []
    for i in operations:
        oper, num = i.split(" ")
        if oper == 'I':
            answer.append(int(num))
        else:
            if len(answer) > 0:
                if num == "1":
                    answer.pop(-1)
                elif num == "-1":
                    answer.pop(0)
        answer.sort()
    if len(answer) == 0:
        return [0, 0]
    else :
        return [max(answer),min(answer)]
