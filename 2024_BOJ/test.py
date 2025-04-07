t = int(input())
a = list(map(int, input().split()))
for p in a:
  is_prime = True
  if p == 1: is_prime = False
  for i in range(2, p):
    if p % i:
      continue
    else:
      is_prime = False
      break
  print('YES' if is_prime else 'NO')