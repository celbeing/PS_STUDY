import sys
input = sys.stdin.readline
fr = 0
for _ in range(int(input())):
    a,b = map(int,input().split())
    if a == 1:
        fr += b
    else:
        if fr < b:
            print("Adios")
            exit()
        else:
            fr -= b
print("See you next month")