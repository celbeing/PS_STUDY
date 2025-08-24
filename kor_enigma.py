import sys
input = sys.stdin.readline

top = 'ㄱ ㄲ ㄴ ㄷ ㄸ ㄹ ㅁ ㅂ ㅃ ㅅ ㅆ ㅇ ㅈ ㅉ ㅊ ㅋ ㅌ ㅍ ㅎ'.split()
mid = 'ㅏ ㅐ ㅑ ㅒ ㅓ ㅔ ㅕ ㅖ ㅗ ㅘ ㅙ ㅚ ㅛ ㅜ ㅝ ㅞ ㅟ ㅠ ㅡ ㅢ ㅣ'.split()
btm = list(' ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ')
base = ord('가')

def korean_sep(word):
    result = []
    for w in list(word.strip()):
        idx = ord(w) - base
        if 0 <= idx <= 11172:
            ch1 = idx // 588
            ch3 = idx % 28
            ch2 = ((idx - ch3) % 588) // 28
            result.append([ch1, ch2, ch3])
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
    enc = korean_enc(sep, 20)
    print(f'{korean_com(enc)}')