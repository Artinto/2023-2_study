def solution(m, n, puddles):
    min_load = m-1+n-1
    current_locations =  [[1, 1]]
    answer = 0
    for a in range(min_load):
        for _ in range(len(current_locations)):
            location = current_locations.pop(0)
            location1, location2 = location, location
            if location[0]+1 <= m:
                location1 = [location[0]+1, location[1]]
            if location1 not in puddles:# and location1 not in current_locations:
                current_locations.append(location1)
            if location[1]+1 <= n:
                location2 = [location[0], location[1]+1]
            if location2 not in puddles:# and location2 not in current_locations:
                current_locations.append(location2)
            if location1 == [m, n] or location2 == [m, n]:
                answer +=1
    return answer
