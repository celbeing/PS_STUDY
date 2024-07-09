import sys
input = sys.stdin.readline
a,b,c,d,e,f = map(int,input().split())
g,h,i,j,k,l = map(int,input().split())

for p in range(g,j):
    if a<=p<d:
        for q in range(h,k):
            if b<=q<e:
                for r in range(i,l):
                    if c<=r<f:
                        print("Yes")
                        exit()

print("No")