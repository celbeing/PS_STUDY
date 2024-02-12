#5639: 이진 검색 트리(tree)
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
pre_order = []
while True:
    try:
        pre_order.append(int(input()))
    except:
        break

n = len(pre_order)

def find(left,right):
    if left > right:
        return
    root = pre_order[left]
    div = right + 1
    for i in range(left+1, right+1):
        if pre_order[i] > root:
            div = i
            break
    find(left+1,div-1)
    find(div,right)
    print(root)

find(0,n-1)