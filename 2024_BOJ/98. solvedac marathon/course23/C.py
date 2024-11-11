#11578: 팀원 모집
import sys
input = sys.stdin.readline
def solution():
    N, M = map(int, input().split())
    can_solve = [list(map(int, input().split()))[1:] for _ in range(M)]
    all_solve = (1 << N) - 1

    def make_team(i, bit, n, rec):
        if bit == all_solve:
            return n
        if n == rec:
            return rec
        for j in range(i + 1, M):
            new_bit = bit
            for p in can_solve[j]:
                new_bit |= 1 << (p - 1)
            rec = make_team(j, new_bit, n + 1, rec)
        return rec

    result = make_team(-1, 0, 0, M + 1)
    if result > M: result = -1
    print(result)
solution()