#1019: 책 페이지
import sys
def solution():
    N = input()
    result = [0] * 10
    digit = len(N) - 1
    for n in N:
        for i in range(int(n)):
            result[i] += 10**digit
            for j in range(10):
                if digit >= 1: result[j] += digit * (10**(digit - 1))
        result[0] -= 10**digit
        if digit:
            result[int(n)] += int(''.join(N[-digit:])) + 1
        else:
            result[int(n)] += 1
        digit -= 1
    print(*result)
solution()