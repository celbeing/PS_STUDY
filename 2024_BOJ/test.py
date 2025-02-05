N = int(input())
input_arr = list(map(int, input().split()))

idx_input_arr = sorted(enumerate(input_arr), key = lambda x : x[1])
# print('input_arr:', idx_input_arr)

diff_arr = [1, 2, 3]
for i in range(3, N):
    a = idx_input_arr[i][1] - idx_input_arr[i-3][1]
    diff_arr.append(a)

dp = [0]*N
dp[3] = diff_arr[3]
assa = [[]]*N
assa[0] = [0]
assa[1] = [0, 1]
assa[2] = [0, 1, 2]
# print('diff_arr: ', diff_arr)
for i in range(4, N):
    a = i % 4
    if a == 3:
        dp[i] = dp[i-4] + diff_arr[i]
    else:
        min_diff = 10**9
        for j in range(a+2):
            if (dp[i-4-j] + diff_arr[i-j]) < min_diff:
                min_diff = dp[i-4-j] + diff_arr[i-j]
                assa[i] = assa[i-4-j] + list(range(i, i-j, -1))
        dp[i] = min_diff


print(dp[N-1])

ans = []
if len(assa[N-1]):
    for elem in assa[N-1]:
        ans.append(idx_input_arr[elem][0])
    ans.sort()
    for elem in ans:
        print(elem)
