import sys
input = sys.stdin.readline

prime = [2,3,5,7,11,13,17,19,23]
pmult = [2,6,30,210,2310,30030,510510,9699690,223092870]

while 1:
    n = int(input())
    if n == 0: break

    result = ""
    result += str(n)+" ="

    p = [0]*10
    for k in range(8,-1,-1):
        if n >= pmult[k]:
            p[k+1] = n//pmult[k]
            n %= pmult[k]
    p[0] = n
    for i in range(10):
        if p[i]:
            if result[-1] == "=":
                result += " "
            else:
                result += " + "
            next = ""
            next += str(p[i])
            for j in range(i):
                next += "*"
                next += str(prime[j])
            result += next
    print(result)