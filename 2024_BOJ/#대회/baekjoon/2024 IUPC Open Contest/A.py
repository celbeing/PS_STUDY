storage = list(input())
r,b,f = 0,0,0
for i in range(10):
    if storage[i] == "@": r = i
    elif storage[i] == "#": b = i
    elif storage[i] == "!": f = i

if r > b > f:
    print(r-f-1)
elif r < b < f:
    print(f-r-1)
else: print(-1)