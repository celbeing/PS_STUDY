#3273: 두 수의 합
import sys, math
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
x = int(input())

count = [0] * 1000001
for i in range(n):
    count[arr[i]] += 1

result = 0

for i in range(1, int((x-0.1)//2+1)):
    result += count[i]*count[x-i]

if x % 2 == 0:
    result += math.comb(count[x//2],2)

print(result)