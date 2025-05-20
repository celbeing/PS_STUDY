# 2730: 오늘은 OS 숙제 제출일
import sys
input = sys.stdin.readline
def is_leap(y):
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                return True
        else:
            return True
    return False

def solution():
    for _ in range(int(input())):
        month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        dl, rp = map(str, input().split())
        m, d, y = map(int, dl.split('/'))
        rm, rd = map(int, rp.split('/'))

        leap = is_leap(y)
        if leap: month[2] += 1

        deadline = sum(month[1:m]) + d
        reported = sum(month[1:rm]) + rd
        if m == 12 and rm == 1:
            reported += 366 if leap else 365
            y += 1
        elif m == 1 and rm == 12:
            deadline += 365
            if leap: reported -= 1
            y -= 1

        if deadline == reported:
            print('SAME DAY')
        elif reported - deadline == 1:
            print(f'{rm}/{rd}/{y} IS 1 DAY AFTER')
        elif 1 < reported - deadline <= 7:
            print(f'{rm}/{rd}/{y} IS {reported - deadline} DAYS AFTER')
        elif deadline - reported == 1:
            print(f'{rm}/{rd}/{y} IS 1 DAY PRIOR')
        elif 1 < deadline - reported <= 7:
            print(f'{rm}/{rd}/{y} IS {deadline - reported} DAYS PRIOR')
        else:
            print('OUT OF RANGE')
    return
solution()