class node:
    def __init__(self):
        self.str = ['\000']*8
        self.arr = [0]*10

def word_sum(str):
    sum = 0
    for c in str:
        if c == '\000' or c == ' ':
            break
        sum += ord(c) - ord('a') + 1
    return sum

def vaildate_input_1(str):
    for c in str:
        if c == '\000':
            break
        if c < 'A' or c > 'Z':
            return False
    return True

def validate_input_2(str):
    key = "TSFHHABP"
    hint = "\\BD_OBNZ"

    prv = 0
    for i in range(8):
        prv = ((prv << 1) ^ str[i]) & 31
        if prv + ord('A' != key[i]):
            return False

    for i in range(8):
        print(chr(str[i]^hint[i]&31))

    return True

def validate_input_3(arr):
    s1 = "computer preferred bulk tourist biographies"
    s2 = "worldwide resistance implemented magical viruses"
    s3 = "theorem"

    def sentence_sum(str):
        sum = 0
        for c in str:
            if c == '\000':
                break
            sum *= 100
            sum += word_sum(str + c) % 100
            while(c != ' ' and c != '\000'):
