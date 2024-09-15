# 문제 정리 - 감옥방 개수가 주어지면 순차적으로 증가하면서

t= int(input())

for _ in range(t):
    n = int(input())
    l = [0]*n
    for i in range(1,n+1): ## i가 하나씩 올라갈 때마다 i의 배수 방들을 열어야 한다.
        for j in range(1,n+1):
            if i*j <=n:
                if l[i * j - 1] == 0:
                    l[i * j - 1] += 1
                else:
                    l[i * j - 1] -= 1
    print(l.count(1))