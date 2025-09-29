import random

name = '김시현 김현중 김하윤 김희주 박소희 서용준 송연우 안병훈 여소영 오윤서 유하은 윤진서 이건우 이건희 이서희 이재건 정우성 정준영 정현정 홍지아'.split()
random.shuffle(name)
for i in range(0, 20, 4):
    print(name[i:i + 4])
