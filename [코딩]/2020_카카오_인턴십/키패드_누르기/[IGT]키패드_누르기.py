def solution(numbers, hand):
    H = {"L": 10, "R": 12}    ## {*}을 10, {#}을 12라고 했을 때, 왼손 엄지와 오른손 엄지의 시작 위치는 각각 10과 12가 된다.
    ans = ""
    for n in numbers:
        if n in [1,4,7]:      ## 문제의 조건에 의해, 1,4,7번 키패드를 누를 때는 왼손 엄지로 누른다.
            H["L"] = n
            ans += "L"
        elif n in [3,6,9]:    ## 문제의 조건에 의해, 3,6,9번 키패드를 누를 때는 오른손 엄지로 누른다.
            H["R"] = n
            ans += "R"
        else:
            if n == 0:        ## 0을 눌러야 하는 경우, 해당 키패드는 11번 키패드라고 가정한다.
                n = 11
            L, R = sum(divmod(abs(H["L"]-n),3)), sum(divmod(abs(H["R"]-n),3))
            ## 현재 엄지손가락의 위치에서 다음 키패드를 누르기 위해 손가락이 이동해야 하는 거리는, 현재 키패드 번호와 눌러야 할 키패드 번호의 차를 3으로 나눠 몫과 나머지를 구한 뒤, 그 둘을 더한 것과 같다.
            ## 왼손 엄지로 누르기 위해 이동해야 하는 거리를 L, 오른손 엄지로 누르기 위해 이동해야 하는 거리를 R이라고 할 때
            if L < R or (L == R and hand[0] == "l"):
            ## L이 R보다 작거나, 혹은 L과 R이 같은데 왼손잡이라면
                ans += "L"
                H["L"] = n
            else:
                ans += "R"
                H["R"] = n
    return ans
