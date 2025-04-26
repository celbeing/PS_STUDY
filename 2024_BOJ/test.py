for _ in range(int(input())):
  card = int(input())
  res = 0
  for _ in range(8):
    res += card % 10
    card //= 10
    k = card % 10
    card //= 10
    k *= 2
    if k >= 10:
      res += k % 10
      k //= 10
      res += k
    else:
      res += k
  if res % 10:
    print('F')
  else:
    print('T')