import sys
input = sys.stdin.readline

t = 'ㄱ ㄲ ㄴ ㄷ ㄸ ㄹ ㅁ ㅂ ㅃ ㅅ ㅆ ㅇ ㅈ ㅉ ㅊ ㅋ ㅌ ㅍ ㅎ'.split()
base = ord('A')

def korean_sep(word):

    result = []
    for w in list(word.strip()):
        idx = ord(w) - base
        if 0 <= idx <= 25:
            result
    return result

def korean_com(sep):
    result = ''
    for ch1, ch2, ch3 in sep:
        ch = base + (ch1 * 21 + ch2) * 28 + ch3
        result += chr(ch)
    return result

def korean_enc(sep, k):
    ret = []
    for ch1, ch2, ch3 in sep:
        ch1 += k
        ch2 += k
        ch3 += k if ch3 else 0
        ch1 %= 19
        ch2 %= 21
        ch3 %= 28
        ret.append([ch1, ch2, ch3])
    return ret

while True:
    origin = input().strip()
    sep = korean_sep(origin)
    enc = korean_enc(sep, 13)
    print(f'{korean_com(enc)}')