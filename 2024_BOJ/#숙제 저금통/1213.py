#1213: 팰린드롬 만들기
import sys
input = sys.stdin.readline
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
hansoo = list(input().rstrip())
even = False
if len(hansoo) % 2 == 0:
    even = True

count = [0 for _ in range(len(alpha))]
for i in hansoo:
    count[alpha.index(i)] += 1

palin = []
if even:
    for i in range(len(alpha)):
        if count[i] % 2 == 1:
            print("I'm Sorry Hansoo")
            exit()
        for j in range(count[i]//2):
            palin.append(alpha[i])
    print(str(''.join(palin)) + str(''.join(reversed(palin))))
else:
    odd = 0
    for i in range(len(alpha)):
        if count[i] % 2 == 1:
            if odd == 0:
                odd = i
            else:
                print("I'm Sorry Hansoo")
                exit()
        for j in range(count[i] // 2):
            palin.append(alpha[i])
    print(str(''.join(palin)) + alpha[odd] + str(''.join(reversed(palin))))