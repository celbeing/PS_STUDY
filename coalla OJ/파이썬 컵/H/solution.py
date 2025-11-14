check = set()
for i in range(1, 10001):
    n = int(input())
    if n in check:
        print("LOSE")
        print(i)
        print(n)
        break
    check.add(n)
else:
    print("WIN")