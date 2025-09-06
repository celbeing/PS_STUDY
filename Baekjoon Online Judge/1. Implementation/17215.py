# 17215: 볼링 점수 계산
import sys
input = sys.stdin.readline
result = list(input().strip())
l_S = 0
ll_S = 0
l_P = 0
score = 0
frame = 1
idx = 0
while frame < 10:
    if result[idx] == 'S':
        score += 10 * (1 + l_S + ll_S + l_P)
        l_P = 0
        ll_S = l_S
        l_S = 1
    else:
        try1, try2 = 0, 0
        if result[idx] != '-':
            try1 = int(result[idx])
        idx += 1
        if result[idx] == 'P':
            try2 = 10 - try1
        elif result[idx] != '-':
            try2 = int(result[idx])
        score += try1 * (1 + l_S + ll_S + l_P) + try2 * (1 + l_S)
        l_P = 1 if try1 + try2 == 10 else 0
        ll_S = l_S = 0
    idx += 1
    frame += 1
if result[idx] == 'S':
    score += 10 * (1 + l_S + ll_S + l_P)
    l_P = 0
    ll_S = l_S
    l_S = 0
    idx += 1
    if result[idx] == 'S':
        score += 10 * (1 + ll_S)
        idx += 1
        if result[idx] == 'S':
            score += 10
        elif result[idx] != '-':
            score += int(result[idx])
    else:
        try1, try2 = 0, 0
        if result[idx] != '-':
            try1 = int(result[idx])
        idx += 1
        if result[idx] == 'P':
            try2 = 10 - try1
        elif result[idx] != '-':
            try2 = int(result[idx])
        score += try1 * (1 + ll_S) + try2
else:
    try1, try2 = 0, 0
    if result[idx] != '-':
        try1 = int(result[idx])
    idx += 1
    if result[idx] == 'P':
        try2 = 10 - try1
    elif result[idx] != '-':
        try2 = int(result[idx])
    score += try1 * (1 + l_S + ll_S + l_P) + try2 * (1 + ll_S)
    if try1 + try2 == 10:
        idx += 1
        if result[idx] == 'S': score += 10
        elif result[idx] != '-': score += int(result[idx])
print(score)