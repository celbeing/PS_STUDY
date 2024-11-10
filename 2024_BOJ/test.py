import sys
input = sys.stdin.readline
def sol(arr, d):
    if d == 6:
        print(arr)
        return 1
    ret = 0
    for i in range(5):
        if i in arr: continue
        elif i == 0 and d in {1, 3, 5}: continue
        elif i == 1 and d == 3: continue
        ret += sol(arr+[i], d + 1)
    return ret
print(sol([],1))