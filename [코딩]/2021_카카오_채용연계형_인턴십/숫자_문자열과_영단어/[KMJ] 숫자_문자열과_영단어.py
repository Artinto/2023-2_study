def solution(word):
    dic = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in dic:
        if i in word:
            word = word.replace(i, str(dic.index(i)))
    answer = int(word)
    return answer
