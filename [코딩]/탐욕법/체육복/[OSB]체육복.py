def solution(n, lost, reserve):
    answer = 0
    lost_items = sorted(lost) # 정렬.
    reserve_items = sorted(reserve) # 정렬.
    temp_reserve = reserve_items.copy()
    answer = n - len(lost_items) 
    for reserve in reserve_items:
        if reserve in lost_items:
            lost_items.remove(reserve)
            temp_reserve.remove(reserve)
            answer+=1
    for lost_item in lost_items:
        if lost_item-1 in temp_reserve:
            temp_reserve.remove(lost_item-1)
            answer +=1
        elif lost_item+1 in temp_reserve:
            temp_reserve.remove(lost_item+1)
            answer+=1
    return answer
