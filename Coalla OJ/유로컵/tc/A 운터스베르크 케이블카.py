"""
탑승 정원 K명인 케이블카를 이용해 N명의 사람이 운터스베르크 산에 오르고자 한다.
케이블카 한 대가 출발 지점에서 정상에 도착했다가 내려오기까지 T초가 걸린다.
케이블카의 운영 시간은 오전 8시 30분부터 오후 5시까지이다.
운영 종료 시각을 넘기 전에 모든 이용객이 출발 지점으로 돌아와야 한다.
N명의 이용객 모두가 오늘 안에 정상을 방문하고 돌아오려면 최소 몇 대의 케이블카가 필요한가?
"""
import random
path = r"C:\Users\kimsd\OneDrive\바탕 화면\tc\\"

for tc in range(1, 11):
    file = open(path + f'{tc}.in', 'w+', encoding='utf-8')
    n = random.randint(1, 1000)
    k = random.randint(1, 10)
    t = random.randint(60, 120)
    w = file.writelines()

    file = open(path + f'{tc}.out', 'w+', encoding='utf-8')
    w = file.writelines()