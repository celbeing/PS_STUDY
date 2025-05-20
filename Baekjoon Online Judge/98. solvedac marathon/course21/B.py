#13022: 늑대와 올바른 단어
import sys
input = sys.stdin.readline
def solution():
    word = list(input().strip())
    n = len(word)
    idx = 0
    while idx < n:
        cnt = 0
        if not word[idx] == 'w': return 0
        while idx < n and word[idx] == 'w':
            cnt += 1
            idx += 1
        for i in range(cnt):
            if idx < n and word[idx] == 'o': idx += 1
            else: return 0
        for i in range(cnt):
            if idx < n and word[idx] == 'l': idx += 1
            else: return 0
        for i in range(cnt):
            if idx < n and word[idx] == 'f': idx += 1
            else: return 0
    return 1
print(solution())