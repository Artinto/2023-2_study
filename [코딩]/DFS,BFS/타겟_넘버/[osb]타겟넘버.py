def solution(numbers, target):
    global answer
    def dfs(idx, sum):
        global answer
        if idx == len(numbers):
            if target == sum:
                answer += 1
            return
        dfs(idx+1, sum - numbers[idx])
        dfs(idx+1, sum + numbers[idx])
    answer = 0
    dfs(0, 0)
    return answer