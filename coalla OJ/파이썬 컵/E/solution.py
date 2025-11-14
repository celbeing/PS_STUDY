y = int(input())
if y % 4 == 0:
    if y % 100:
        if y % 400:
            print(366)
        else:
            print(365)
    else:
        print(366)
else:
    print(365)