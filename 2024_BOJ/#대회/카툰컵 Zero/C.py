#C: 생일 축하합니다~
import sys
input = sys.stdin.readline
N = int(input())
name = [input().rstrip() for _ in range(N)]
for a in name:
    print("? {}".format(a))
    k = int(input())
    sys.stdout.flush()
    if k == 0 and not lied:
        print("? {}".format(a))
        k = int(input())
        sys.stdout.flush()
        if k == 1:
            lied = True
            print("? {}".format(a))
            k = int(input())
            sys.stdout.flush()
            if k == 1:
                print("! {}".format(a))
                sys.stdout.flush()
                exit()

    elif k == 0 and lied:
        continue
    elif k == 1 and not lied:
        print("? {}".format(a))
        k = int(input())
        sys.stdout.flush()
        if k == 1:
            print("! {}".format(a))
            sys.stdout.flush()
            exit()
        else:
            lied = True
    elif k == 1 and lied:
        print("! {}".format(a))
        sys.stdout.flush()
        exit()