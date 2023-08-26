def solution(array, commands):
    answer = []
    for command in commands:
        start, end, target = command
        sliced = sorted(array[start-1:end])
        answer.append(sliced[target-1])
    return answer
