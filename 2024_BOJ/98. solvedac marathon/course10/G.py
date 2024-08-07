#2922: 즐거운 단어
import sys
input = sys.stdin.readline
word = list(input().rstrip())
n = len(word)
cont = [1,21,441,9261,194481,4084101,85766121,1801088541,37822859361,794280046581,16679880978201]
cont_l = [1,20,400,8000,160000,3200000,64000000,1280000000,25600000000,512000000000,10240000000000]
vowel = [1,5,25,125,625,3125,15625,78125,390625,1953125,9765625]
L = True
for i in range(n):
    if word[i] == "_": word[i] = 0
    elif ord(word[i]) in (65,69,73,79,85): word[i] = 1
    else:
        if word[i] == "L": L = False
        word[i] = 2

def cal(c,v):
    ret = cont[c]*vowel[v]
    if L: ret -= cont_l[c]*vowel[v]
    return ret

def check(k,i):
    if i >= 2 and (k[i-2] == k[i-1] == k[i]):
        return False
    return True

def bt(k,i,c,v):
    if i == n:
        global res
        res += cal(c,v)
        return

    if k[i] == 0:
        k[i] = 2
        if check(k,i):
            bt(k,i+1,c+1,v)
        k[i] = 1
        if check(k,i):
            bt(k,i+1,c,v+1)
        k[i] = 0
    else:
        if check(k,i):
            bt(k,i+1,c,v)
    return

res = 0
bt(word[:],0,0,0)
print(res)