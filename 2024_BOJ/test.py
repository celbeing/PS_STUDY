import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    print("even" if n & 2 else "odd")
    
while True:
    solution()