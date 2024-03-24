import time
li = [0,1,1,1,0,0,1,1,0,0,1,1,1]
res = []

start = time.time()
s,e = 0,0
while s < len(li):
    while li[s] == 0: s += 1
    e = s
    while e<len(li) and li[e] == 1: e += 1
    res.append(e-s)
    s = e
print(res)
print(f"실행시간 {time.time()-start:.10f}")

start = time.time()
li = [0,1,1,1,0,0,1,1,0,0,1,1,1]
res = []
cnt = 0
for num in li:
  if num:
    cnt += 1
  elif cnt:
    res.append(cnt)
    cnt = 0
if cnt:
  res.append(cnt)
print(res)
print(f"실행시간 {time.time()-start:.10f}")