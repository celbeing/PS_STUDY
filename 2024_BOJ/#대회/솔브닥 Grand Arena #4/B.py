#B번 - 정렬된 연속한 부분수열의 개수
import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
result = 0
increase = 1
for i in range(N-1):
    if A[i] < A[i+1]:
        increase += 1
    else:
        result += increase*(increase+1)//2
        increase = 1
result += increase*(increase+1)//2
print(result)