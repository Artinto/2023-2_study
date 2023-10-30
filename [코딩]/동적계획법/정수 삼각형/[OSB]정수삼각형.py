def solution(triangle):
    answer = 0
    depth = len(triangle)
    number_list = [[triangle[0][0], 0]]
    for index in range(1, depth):
        numbers  = triangle[index]
        for tmp in number_list[2**(index-1)-1:2**(index)-1]:
            number_list.append([tmp[0]+numbers[tmp[1]], tmp[1]])
            number_list.append([tmp[0]+numbers[tmp[1]+1], tmp[1]+1])
    answer = max(number_list)
    return answer[0]
