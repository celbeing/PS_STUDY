p = [0, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
'''dp = [0] * 101
dp[0] = 1
for i in range(1, 26):
    for j in range(p[i], 101):
        dp[j] += dp[j - p[i]]
print(dp[int(input())])'''


count = 0
def dfs(i, r):
    for j in range(i + 1, 26):
        for k in range(p[j], r + 1, p[j]):
            if r - k == 0:
                global count
                count += 1
                break
            dfs(j, r - k)
dfs(0, int(input()))
print(count)
