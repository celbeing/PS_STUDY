#15720: 카우버거
import sys
input = sys.stdin.readline
def solution():
    B, C, D = map(int, input().split())
    burger = sorted(list(map(int, input().split())), reverse = True)
    side = sorted(list(map(int, input().split())), reverse = True)
    drink = sorted(list(map(int, input().split())), reverse = True)
    total = sum(burger + side + drink)
    set_count = min(min(B, C), D)
    discount = sum(burger[:set_count] + side[:set_count] + drink[:set_count]) // 10
    print(total)
    print(total - discount)
solution()