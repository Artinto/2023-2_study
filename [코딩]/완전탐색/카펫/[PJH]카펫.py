def solution(brown, yellow):
    total_size = brown + yellow

    for i in range(1, int(total_size**0.5) + 1): # int(total_size**0.5)는 int로 인해 내림 적용
        if total_size % i == 0: # 나머지가 0인 값을 조건으로 width가 될 수 있는 값을 찾음
            width = total_size // i
            height = i
            
            if (width - 2) * (height - 2) == yellow: # 위 조건문에서 나온 width값을 기준으로 width, height에 두칸씩 빼서 곱한 값이 yellow와 같은 지 확인 후 return
                return [width, height]
 
