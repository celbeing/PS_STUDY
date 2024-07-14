a,b = map(int,input().split())
c,d = map(int,input().split())
e,f = map(int,input().split())
A = (a-c)**2+(b-d)**2
B = (c-e)**2+(d-f)**2
C = (e-a)**2+(f-b)**2
if A == B+C or B == A+C or C == A+B:
    print("Yes")
else:
    print("No")