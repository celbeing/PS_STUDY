N = int(input())
if N < 10: print(1)
else:
    for i in range(2, 10):
        for j in range(1, 10):
            if N == i * j:
                print(1)
                exit()
    print(0)