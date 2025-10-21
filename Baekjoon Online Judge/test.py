from random import shuffle

seed = list(map(str, '선생님 김하윤 김현중 유하은 정우성 윤진서 정준영 정현정'.split()))
player = list(map(str, '김시현 서용준 송연우 안병훈 오윤서 이건우 이건희 이재건'.split()))
shuffle(player)
for i in range(0, 8, 2):
    print(f'{seed[i]}-{player[i]}')
    print(f'{player[i + 1]}-{seed[i + 1]}')