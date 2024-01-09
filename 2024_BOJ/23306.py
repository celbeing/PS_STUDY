#23306: Binary는 호남선
import sys
N = int(input())
print("? 1")
start = int(input())
sys.stdout.flush()
print("? {}".format(N))
end = int(input())
sys.stdout.flush()
if start == end:
    print("! 0")
elif start == 1:
    print("! -1")
else:
    print("! 1")