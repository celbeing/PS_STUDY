import sys
input = sys.stdin.readline
i = 0
while 1:
    i += 1
    flag = 0 if i % 29 else 1
    a = i // 10
    b = i % 10
    c = 0 if (a + b * 3) % 29 else 1
    if flag == c:
        if flag:
            print(f'{i}는 29의 배수')
        else:
            print(f'{i}에 대해 통과')
    else:
        print(f'반례는 {i}')
        input('계속')