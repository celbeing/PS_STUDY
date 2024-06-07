N,L,R = map(int,input().split())
A = [i for i in range(1,L)]
A += [i for i in range(R,L-1,-1)]
A += [i for i in range(R+1,N+1)]
print(*A)