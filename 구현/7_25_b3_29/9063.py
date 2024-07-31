num = int(input())
maxX = -100000000
minX = 100000000

maxY = -100000000
minY = 100000000
## 음수인 경우도 고려해야 한다

for i in range(num):
    x,y = map(int,input().split())
    if x>maxX :
        maxX=x
    if x<minX :
        minX=x
    if y>maxY:
        maxY=y
    if y<minY:
        minY=y

print((maxX-minX)*(maxY-minY))