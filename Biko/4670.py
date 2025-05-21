# 4670: 보물찾기
for _ in range(int(input())):
    l, r, s = map(int, input().split())
    l = s - l
    r -= s
    if l < r: print(l * 2 + 1)
    else: print(r * 2)