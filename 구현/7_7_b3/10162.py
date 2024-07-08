sec = int(input())

A,B,C = 0, 0 , 0

if sec % 10 == 0:
    if sec ==0:
        print(0)
        exit()
    if sec >= 300:
        while sec >=300:
            sec = sec - 300
            A += 1
    if sec >= 60:
        while sec >= 60:
            sec = sec - 60
            B += 1
    if sec != 0:
        while sec != 0:
            sec = sec - 10
            C += 1
    print(A, end=" ")
    print(B, end=" ")
    print(C, end=" ")

else:
    print(-1)

#특정 조건에서 특정 코드 스킵하고 싶으면 이중 if문을 해야되는 것임.
# 2회이상 빼야되는 것도 고려해야 됨

