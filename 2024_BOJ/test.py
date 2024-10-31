def solution():
    melody = list(input().strip())
    l = len(melody)
    count = 0
    for i in range(1, (l + 1) // 2):
        if (l - i) % (i + 1): continue
        flag = False
        for j in range(i, l, i + 1):
            m, v = 0, j
            for k in range(i + 1):
                if melody[m] == melody[v]:
                    m += 1
                    v += 1
                elif flag: break
                else:
                    flag = True
                    v += 1
            else:
                flag = False
            if flag:
                break
        else:
            count += 1
    print(count)
solution()