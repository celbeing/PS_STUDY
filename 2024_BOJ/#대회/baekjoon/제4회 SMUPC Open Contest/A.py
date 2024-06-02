n,s = input().split()
N = int(n)
S = list(s)
alpha = set()
count = 0
newS = []
for i in range(len(S)):
    if S[i] in alpha:
        count += 1
    else:
        newS.append(S[i])
        alpha.add(S[i])
newS += list(str(count+4))
S = list(str(1906+N))+newS
S.reverse()
S = list("smupc_")+S
print(*S,sep='')