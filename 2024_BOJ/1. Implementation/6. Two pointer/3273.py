#3273: 두 수의 합
import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int,input().split())))
x = int(input())

l = 0
r = n-1
result = 0

while l < r:
    if arr[l]+arr[r] < x:
        l+=1
    elif arr[l]+arr[r] > x:
        r-=1
    else:
        l+=1
        r-=1
        result+=1

print(result)