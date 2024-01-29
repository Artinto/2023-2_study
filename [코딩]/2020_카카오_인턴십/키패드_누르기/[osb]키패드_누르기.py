def solution(numbers, hand):
    answer = ''
    left_floor = 4
    left_po = 1
    right_po = 3
    right_floor = 4
    floor = dict() # 층 딕셔너리
    for num in range(1, 10):
        floor[num] = (num-1)//3 + 1
    floor[0] = 4
    
    for num in numbers:
        if num in [1, 4, 7]:
            answer += 'L'
            left_floor = floor[num] # 왼손 위치 조정.
            left_po = 1
            
        elif num in [3, 6, 9]:
            answer += 'R'
            right_floor = floor[num] # 오른손 위치 조정.
            right_po = 3
        else: # 가운데 
            move_to = floor[num] # 눌러야할 번호
            left_sub = abs(move_to-left_floor)+abs(2-left_po)
            right_sub = abs(move_to-right_floor)+abs(2-right_po)
            if right_sub > left_sub:
                answer += 'L'
                left_floor = floor[num] # 왼손 위치 조정.
                left_po = 2
            elif right_sub < left_sub:
                answer += 'R'
                right_floor = floor[num] # 오른손 위치 조정.
                right_po = 2
            else:
                if hand == 'left':
                    answer += 'L'
                    left_floor = floor[num] # 오른손 위치 조정.
                    left_po = 2
                else:
                    answer += 'R'
                    right_floor = floor[num] # 오른손 위치 조정.
                    right_po = 2
    return answer