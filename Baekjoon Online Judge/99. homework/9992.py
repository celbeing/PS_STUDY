# 9992: 비밀 메시지
import sys
input = sys.stdin.readline

s = list(input().strip())
n = len(s)
limit = (n + 1) >> 1

count = 0
for l in range(1, limit):
    # 뒤를 삭제하고 앞에 붙인 경우
    for i in range(l):
        if s[i] == s[i + l]: continue
        else: break
    else: count += 1

    # 뒤를 삭제하고 뒤에 붙인 경우
    # 앞을 삭제하고 앞에 붙인 경우
    for i in range(l):
        if s[n - l + i] == s[i]: continue
        else: break
    else: count += 2

    # 앞을 삭제하고 뒤에 붙인 경우
    for i in range(l):
        if s[n - (l * 2) + i] == s[n - l + i]: continue
        else: break
    else: count += 1
print(count % 2014)

# 아 이거 아니네