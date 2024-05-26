K = int(input())
pic = ["G...",".I.T","..S."]
for l in pic:
    new_l = ""
    for c in l:
        new_l += c*K
    for _ in range(K):
        print(new_l)