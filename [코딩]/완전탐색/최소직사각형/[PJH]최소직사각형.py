def solution(sizes):
    max_w = max_h = 0
    for w, h in sizes:
        if w < h:  
            w, h = h, w
        if w > max_w:
            max_w = w
        if h > max_h:
            max_h = h

    return max_w * max_h
