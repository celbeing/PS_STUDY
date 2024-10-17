#14725: 개미굴
import sys
input = sys.stdin.readline

class Node(object):
    def __init__(self, end = False):
        self.is_end = end
        self.children = dict()

class Trie(object):
    def __init__(self):
        self.head = Node()

    def insert(self, words):
        current_node = self.head
        for word in words:
            if current_node.children.get(word) is None:
                current_node.children[word] = Node()
            current_node = current_node.children[word]
        current_node.is_end = True

    def search(self, words):
        current_node = self.head
        for word in words:
            if current_node.children.get(word) is None:
                return False
            current_node = current_node.children[word]
        return True

    def result(self, depth, now):
        if now.is_end: return
        child = sorted(now.children)

        for next in child:
            print("--" * depth + next)
            self.result(depth + 1, now.children[next])

def solution():
    N = int(input())
    cave = Trie()
    for _ in range(N):
        cave.insert(list(map(str, input().split()))[1:])
    cave.result(0, cave.head)

solution()