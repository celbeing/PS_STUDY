#27065: 2022년이 아름다웠던 이유
import sys
input = sys.stdin.readline
arr = [1]*5001
for i in range(2,5001):
    for j in range(i,5001,i):
        arr[j] += i
for _ in range(int(input())):
    n = int(input())
    flag = False
    if arr[n] > n<<1:
        flag = True
        for k in range(1,n):
            if n % k == 0 and arr[k] > k<<1:
                flag = False
                break
    if flag:
        print("Good Bye")
    else:
        print("BOJ 2022")