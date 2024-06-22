n = int(input())
used = 0
h = 0
while n >= used:
    used += (h**2+h)*2+1
    h += 1
print(h-1)