path = "C:\\Users\\kimsd\\Desktop\\"
file_no = 1
while True:
    i = input()
    file = open(path + f"{file_no}.in", 'w')
    w = file.writelines(f'{i}')
    p, q = map(str, i.split())
    file = open(path + f"{file_no}.out", 'w')
    w = file.writelines(f'{p}\n{q}')
    file_no += 1