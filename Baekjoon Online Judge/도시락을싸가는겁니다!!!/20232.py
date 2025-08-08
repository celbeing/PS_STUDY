# 20232: Archivist
import sys
input = sys.stdin.readline
def solution():
    winner = dict()
    for i in range(1995, 2020): winner[i] = 'ITMO'
    spbsu = [1996, 1997, 2000, 2007, 2008, 2013, 2018]
    for s in spbsu: winner[s] = 'SPbSU'
    winner[2006] = 'PetrSU, ITMO'
    print(winner[int(input())])
solution()