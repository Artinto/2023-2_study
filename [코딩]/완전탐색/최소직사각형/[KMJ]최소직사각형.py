def solution(sizes):
    big = []
    small = []
    for width, height in sizes:
        if width >= height:
            big.append(width)
            small.append(height)
        else:
            big.append(height)
            small.append(width)
    answer = max(big) * max(small)
    return answer
