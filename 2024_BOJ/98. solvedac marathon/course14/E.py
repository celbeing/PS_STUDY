#29768: 팰린드롬 이름
import sys
input = sys.stdin.readline
def solution():
    N, K = map(int, input().split())
    alpha = list("a b c d e f g h i j k l m n o p q r s t u v w x y z".split())
    res = ""
    for i in range(N-K):
        res += "a"
    for i in range(K):
        res += alpha[i]
    print(res)
solution()