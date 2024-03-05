def time_convert(time):
    x,y,z = map(int,time.split(':'))
    return 3600*x + 60*y + z
def solution(play_time, adv_time, logs):
    play_time = time_convert(play_time)
    table = [0]*(play_time+1)
    adv_time = time_convert(adv_time)
    for l in logs:
        start,end = map(time_convert,l.split('-'))
        table[start] += 1
        table[end] -= 1
    prefix_sum = [0,table[0]]
    for i in range(1,len(table)):
        table[i] += table[i-1]
        prefix_sum += [prefix_sum[-1] + table[i]]
    max_sum = 0
    for i in range(play_time-adv_time+1):
        s = prefix_sum[i+adv_time]-prefix_sum[i]
        if s > max_sum:
            t = i
            max_sum = s
    h,m,s = str(t//3600).zfill(2),str(t%3600//60).zfill(2),str(t%3600%60).zfill(2)
    return "{}:{}:{}".format(h,m,s)
