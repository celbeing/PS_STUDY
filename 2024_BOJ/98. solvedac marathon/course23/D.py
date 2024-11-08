#1695: 팰린드롬 만들기
import sys
input = sys.stdin.readline
def solution():
    N = int(input())
    arr = list(map(int, input().split()))
    ldp, rdp = [0] * 