r,g,b = map(int,input().split())
C = input()
if C == "Blue":
    print(min(r,g))
elif C == "Red":
    print(min(g,b))
else:
    print(min(r,b))