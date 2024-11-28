# 24813: The Grand Adventure
import sys
input = sys.stdin.readline
def solution():
    for _ in range(int(input())):
        bag = []
        obj = {'$':1,'|':2,'*':3}
        things = ('$', '|', '*')
        adv = list(input().rstrip())
        for k in adv:
            if k in things: bag.append(obj[k])
            elif k == '.': continue
            elif k == 'b' and bag and bag.pop() == 1: continue
            elif k == 't' and bag and bag.pop() == 2: continue
            elif k == 'j' and bag and bag.pop() == 3: continue
            else:
                print("NO")
                break
        else:
            if bag: print("NO")
            else: print("YES")
solution()