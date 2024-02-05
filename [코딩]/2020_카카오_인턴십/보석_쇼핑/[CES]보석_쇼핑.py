def solution(gems):
    gems_kind = set(gems)

    if len(gems_kind) == 1:
        return [1, 1]

    lp, rp = 0, 0
    answer = [1, len(gems)]
    gems_dict = dict()
    gems_dict[gems[0]] = 1
    while lp < len(gems) and rp < len(gems):
        if len(gems_dict) == len(gems_kind):
            if answer[1] - answer[0] > rp - lp:
                answer = [lp+1, rp+1]
            if gems_dict[gems[lp]] != 1:
                gems_dict[gems[lp]] -= 1
            else:
                del gems_dict[gems[lp]]
            lp += 1
        else:
            rp += 1
            if rp >= len(gems):
                break
            if not gems[rp] in gems_dict:
                gems_dict[gems[rp]] = 1
            else:
                gems_dict[gems[rp]] += 1
    return answer
