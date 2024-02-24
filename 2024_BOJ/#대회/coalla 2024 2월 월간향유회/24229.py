#24229: 모두싸인 출근길
import sys
input = sys.stdin.readline
N = int(input())
board = sorted([tuple(map(int,input().split())) for _ in range(N)])
juhun = []
record = 0
index = 0