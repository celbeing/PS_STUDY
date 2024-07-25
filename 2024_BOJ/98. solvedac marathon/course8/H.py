import sys
input = sys.stdin.readline
words = [0]*int(input())
full = (1<<26)-1
for i in range(len(words)):
    n = list(input().rstrip())
    for k in n:
        words[i] |= 1<<(25-ord(k)+97)

def test(depth,now):
    ret = 0
    if now == full: ret += 1
    for i in range(depth+1,len(words)):
        ret += test(i,now|words[i])
    return ret

print(test(-1,0))