# 25796: 초콜릿 나눠 팔기
import sys
input = sys.stdin.readline
mod = int(1e9 + 7)
dp1 = [0] * 50001
dp2 = [0] * 50001
dp1[0], dp2[0] = 1, 1
ps1, ps2 = 1, 1
for i in range(1, 50001):
    dp1[i] = dp1[i - 1] + (ps1 << 1)
    dp1[i] %= mod
    ps1 += dp1[i]

    dp2[i] = dp2[i - 1] + (ps2 << 1) + 1
    dp2[i] %= mod
    ps2 += dp2[i]

for _ in range(int(input())):
    n, r, c = map(int, input().split())

    # 해를 구성할 수 없는 경우
    if (r + c) & 1:
        print(0)
        continue

    # 가운데가 뚫린 경우
    elif r == 2:
        res = (dp2[(c - 2) >> 1] * dp2[(n - c) >> 1] * 2) % mod
        print(res)

    # 나머지 경우
    else:
        res = (dp1[c >> 1] * dp2[(n - c) >> 1] + dp1[(n - c) >> 1] * dp2[c >> 1] - dp1[c >> 1] * dp1[(n - c) >> 1]) % mod
        print(res)