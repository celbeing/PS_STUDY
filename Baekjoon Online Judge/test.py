n = int(input())
s = list(input().strip())
for i in range(n):
    s[i] = 'L' if s[i] == 'l' else 'i'
print(''.join(s))