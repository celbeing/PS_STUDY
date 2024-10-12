#13635 Concurso de Contos
import sys
input = sys.stdin.readline
def solution():
    while True:
        pages = input()
        if pages == "": break
        N, L, C = map(int, pages.split())
        p, l, w = 1, 1, 0
        sentence = list(map(str, input().split()))
        for word in sentence:
            length = len(word)
            w += length
            if w > C:
                if l == L:
                    p += 1
                    l = 1
                else:
                    l += 1
                w = length
            w += 1
        print(p)
solution()