n,m,k,a,b,c = map(int,input().split())
kings = []
kings.append(("Joffrey",n*a))
kings.append(("Robb",m*b))
kings.append(("Stannis",k*c))
kings.sort(key = lambda x: (-x[1],x[0]))
while kings[0][1] > kings[-1][1]: kings.pop()
if len(kings) == 1:
    print(kings[0][0])
elif len(kings) == 2:
    print(kings[0][0],kings[1][0])
else:
    print(kings[0][0],kings[1][0],kings[2][0])