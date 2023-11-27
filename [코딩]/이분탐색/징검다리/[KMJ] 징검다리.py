def solution(distance, rocks, n):
    rocks.sort()
    start, end = 0, distance
    
    while start <= end:
        mid = ( start + end ) // 2
        count = 0
        cur = 0
        for i in range (len(rocks)):
            pre = rocks[i]
            
            if pre - cur < mid:
                count += 1
            else:
                cur = pre
            if n < count:
                break
        if count <= n:
            answer = mid
            start = mid +1
        else:
            end = mid - 1
            
    return answer
