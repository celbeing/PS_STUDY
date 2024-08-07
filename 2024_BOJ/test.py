def euc(a,b):
    while b:
        a,b = b,a%b
    return a

print(euc(-9,-3))
print(-2415//3)