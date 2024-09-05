#32154: SUAPC 2024 Winter
import sys
input = sys.stdin.readline
def solution():
    N = int(input())
    solved = [[],['A','B','C','D','E','F','G','H','J','L','M'],['A','C','E','F','G','H','I','L','M'],
              ['A','C','E','F','G','H','I','L','M'],['A','B','C','E','F','G','H','L','M'],
              ['A','C','E','F','G','H','L','M'],['A','C','E','F','G','H','L','M'],
              ['A','C','E','F','G','H','L','M'],['A','C','E','F','G','H','L','M'],
              ['A','C','E','F','G','H','L','M'],['A','B','C','F','G','H','L','M']]
    print(len(solved[N]))
    print(*solved[N])
solution()