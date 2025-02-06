# 구현 문제: 풀이는 떠올리기 쉽지만 소스코드로 옮기기 어려운 문제
# 상하좌우

N = int(input())

l = list(input().split())

x,y=1,1

for i in l:
    if 'L' == i:
        if x==1 :
            pass
        else:
            x -= 1
    elif 'R' == i :
        if x == N :
            pass
        else:
            x += 1
    elif 'U' == i:
        if y == 1 :
            pass
        else:
            y -= 1
    else:
        if y == N :
            pass
        else:
            y += 1
print(x,y)

