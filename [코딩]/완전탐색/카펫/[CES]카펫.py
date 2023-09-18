def solution(brown, yellow):
    total_size = brown + yellow

    for i in range(1, int(total_size**0.5) + 1): 
        if total_size % i == 0: 
            width = total_size // i
            height = i
            
            if (width - 2) * (height - 2) == yellow: 
                return [width, height]
 
