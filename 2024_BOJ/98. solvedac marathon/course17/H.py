#25970: 현대 모비스 에어 서스펜션
import sys
input = sys.stdin.readline
def solution():
    B = int(input())
    low = [input().rstrip() for _ in range(B)]
    high = [input().rstrip() for _ in range(B)]
    for _ in range(int(input())):
        data = input().rstrip()
        l = len(data)
        c = 0
        for i in range(B):
            k = len(low[i])
            for j in range(l - k + 1):
                if data[j:j + k] == low[i]:
                    c -= 1
            k = len(high[i])
            for j in range(l - k + 1):
                if data[j:j + k] == high[i]:
                    c += 1
        if c > 0: print(f"LOW {c}")
        elif c < 0: print(f"HIGH {-c}")
        else: print("GOOD")
solution()