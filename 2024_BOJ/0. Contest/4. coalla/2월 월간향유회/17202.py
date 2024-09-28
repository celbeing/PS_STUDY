#17202: 핸드폰 번호 궁합
import sys
input = sys.stdin.readline

phone1 = list(input().rstrip())
phone2 = list(input().rstrip())
test = []

for i in range(8):
    test.append(int(phone1[i]))
    test.append(int(phone2[i]))

for i in range(14):
    for j in range(15,i,-1):
        test[j] += test[j-1]
        test[j] %= 10

print("{}{}".format(test[-2],test[-1]))