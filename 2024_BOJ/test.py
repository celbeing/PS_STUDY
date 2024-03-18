N = int(input())
s = [False]*10
A = list(map(int,input().split()))
for k in A:
    s[k] = True
for i in range(10):
    if s[i]:
        print(i)