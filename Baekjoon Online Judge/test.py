count = 0
cases = dict()
for i in range(1, 47):
    for j in range(i, 47):
        t = i + j * 23
        if not(t in cases):
            count += 1
            cases[t] = (i, j)
        else:
            print(f'the case {i} and {j} already added by {cases[t]}')
print(count)