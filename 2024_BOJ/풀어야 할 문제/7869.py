#7869: 두 원
import sys
input = sys.stdin.readline
xa,ya,ra,xb,yb,rb = map(float,input().split())
d = ((xa-xb)**2+(ya-yb)**2)**0.5
area = 0