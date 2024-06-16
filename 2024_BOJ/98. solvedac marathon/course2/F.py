import sys
input = sys.stdin.readline
city = []
dist = []
temp = list(map(str,"Seoul 0.0,Yeongdeungpo 9.1,Anyang 23.9,Suwon 41.5,Osan 56.5,Seojeongri 66.5,Pyeongtaek 75.0,Seonghwan 84.4,Cheonan 96.6,Sojeongni 107.4,Jeonui 114.9,Jochiwon 129.3,Bugang 139.8,Sintanjin 151.9,Daejeon 166.3,Okcheon 182.5,Iwon 190.8,Jitan 196.4,Simcheon 200.8,Gakgye 204.6,Yeongdong 211.6,Hwanggan 226.2,Chupungnyeong 234.7,Gimcheon 253.8,Gumi 276.7,Sagok 281.3,Yangmok 289.5,Waegwan 296.0,Sindong 305.9,Daegu 323.1,Dongdaegu 326.3,Gyeongsan 338.6,Namseonghyeon 353.1,Cheongdo 361.8,Sangdong 372.2,Miryang 381.6,Samnangjin 394.1,Wondong 403.2,Mulgeum 412.4,Hwamyeong 421.8,Gupo 425.2,Sasang 430.3,Busan 441.7".split(',')))
for k in temp:
    c,d = map(str,k.split())
    city.append(c)
    dist.append(float(d))
N,Q = map(int,input().split())
date = 0
last = -1
time = [[-1]*2 for _ in range(43)]
for i in range(N):
    data = list(map(str,input().split()))
    sta = city.index(data[0])
    if data[1] == "-:-":
        hs,ms = 0,0
    else:
        hs,ms = map(int,data[1].split(':'))
    if data[2] == "-:-":
        he,me = 0,0
    else:
        he,me = map(int,data[2].split(':'))
    if hs*60+ms + date <= last: date = 1440
    time[sta][0] = hs*60+ms+date
    time[sta][1] = he*60+me+date
    last = time[sta][1]
for i in range(Q):
    s,e = map(str,input().split())
    sta_s = city.index(s)
    sta_e = city.index(e)
    distance = abs(dist[sta_e]-dist[sta_s])
    timetake = (time[sta_e][0]-time[sta_s][1])
    print(distance*60/timetake)