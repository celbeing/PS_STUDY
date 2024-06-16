import sys
input = sys.stdin.readline

class Node:
    def __init__(self,key,data=None):
        self.key = key
        self.data = data
        self.child = {}

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, str):
        cnt = self.head
        for c in str:
            if c not in cnt.child:
                cnt.child[c] = Node(c)
            cnt = cnt.child[c]
        cnt.data = str

    def search(self, str):
        cnt = self.head
        for c in str:
            if c in cnt.child:
                cnt = cnt.child[c]
            else:
                return False
        return bool(cnt.child)

t = int(input())
for _ in range(t):
    n = int(input())
    trie = Trie()
    num = []
    for _ in range(n):
        k = input().rstrip()
        trie.insert(k)
        num.append(k)

    for k in num:
        if trie.search(k):
            print("NO")
            break
    else: print("YES")