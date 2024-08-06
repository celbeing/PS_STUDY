#9057: ACM-UCPC
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    result = []
    s_count = {}
    for _ in range(int(input())):
        team,school,solved,penalty = map(str,input().split())
        result.append((team,school,int(solved),int(penalty)))
    result.sort(key = lambda x: (-x[2],x[3]))
