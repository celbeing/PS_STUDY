#26099: 설탕 배달 2
N = int(input())
if N == 4 or N == 7: print(-1)
elif N % 5 == 0: print(N // 5)
else: print(N // 5 + (N % 5 - 1) % 2 + 1)