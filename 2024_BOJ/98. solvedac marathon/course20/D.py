#14965: Lozinke
import sys
from collections import defaultdict
input = sys.stdin.readline
def solution():
    count = defaultdict(int)
    pw = []
    n = int(input())
    for _ in range(n):
        string = input().rstrip()
        pw.append(string)
        sub_string = set()
        l = len(string)
        for i in range(l):
            cnt_sub_string = ''
            for j in range(i, l):
                cnt_sub_string += string[j]
                sub_string.add(cnt_sub_string)
        for cnt_sub_string in sub_string:
            count[cnt_sub_string] += 1
    result = 0
    for i in range(n):
        result += count[pw[i]]
    result -= n
    print(result)
solution()