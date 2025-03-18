# 18109: 도깨비불
import sys
input = sys.stdin.readline
def solution():
    conso = 'qwertasdfgzxcvQWERT'
    vowel = 'yuiophjklbnmOP'
    c_check = False
    v_check = False
    f_check = False
    count = 0

    word = list(input().strip())
    for w in word:
        if w in conso:
            if c_check and v_check:
                if f_check:
                    c_check = True
                    v_check = False
                else: f_check = True