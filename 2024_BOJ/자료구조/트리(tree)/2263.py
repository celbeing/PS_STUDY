#2263: 트리의 순회
import sys
sys.setrecursionlimit(100001)
input = sys.stdin.readline
n = int(input())
inorder = list(map(int,input().split()))
postorder = list(map(int,input().split()))
index = dict()
for i in range(n):
    index[inorder[i]] = i
tree = []

def rootfind(il, ir, pl, pr):
    if il <= ir and pl <= pr:
        root = postorder[pr]
        tree.append(root)
        i_div = index[root]
        p_div = i_div-il+pl
        if il < ir and pl < pr:
            rootfind(il,i_div-1,pl,p_div-1)
            rootfind(i_div+1,ir,p_div,pr-1)
    return

rootfind(0,n-1,0,n-1)
print(*tree)