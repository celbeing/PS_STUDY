def solution():
    n = int(input())
    small = [1, 4, 10, 20, 35, 56, 83, 116, 155, 198, 244, 292]
    if n < 12: print(small[n])
    else: print(n * 49 - 247)
solution()