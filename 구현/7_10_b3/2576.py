sumnum =0
minnum =100

for _ in range(7):
    n = int(input())
    if n % 2 != 0:
        sumnum += n
        if minnum > n:
            minnum= n

if sumnum == 0:
    print(-1)
else:
    print(sumnum)
    print(minnum)

