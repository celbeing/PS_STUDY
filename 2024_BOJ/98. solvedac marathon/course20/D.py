#14965: Lozinke
# 필요한 라이브러리 import
from collections import defaultdict

# 변수 초기화
s = set()
mp = defaultdict(int)
arr = []


# 메인 함수
def main():
    n = int(input())  # 입력받기
    for i in range(n):
        str_input = input().strip()
        arr.append(str_input)
        s.clear()

        sz = len(str_input)
        for j in range(sz):
            sub = ""
            for k in range(j, sz):
                sub += str_input[k]
                s.add(sub)

        for sub in s:
            mp[sub] += 1

    ans = 0
    for i in range(n):
        ans += mp[arr[i]]

    ans -= n
    print(ans)


# 메인 함수 실행
if __name__ == "__main__":
    main()
