dodeca = 'ABCDEFGHIJKL'
n = int(input()) - 1
res = dodeca[n % 12] + str(n % 10)
print(res)