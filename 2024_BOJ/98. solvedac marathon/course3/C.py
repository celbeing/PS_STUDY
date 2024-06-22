import sys
input = sys.stdin.readline
K,L = map(int,input().split())
wait = dict()
rank = 1
for _ in range(L):
    stu = input().rstrip()
    wait[stu] = rank
    rank += 1
order = []
for stu in wait: order.append((wait[stu],stu))
order.sort()
for i in range(min(K,len(order))):
    print(order[i][1])