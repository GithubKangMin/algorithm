N,M = map(int, input().split())
arraya =[]
arrayb =[]
newarray = []

for row in range(N):
    col = list(map(int,input().split()))
    arraya.append(col)

for row in range(N):
    col = list(map(int,input().split()))
    arrayb.append(col)

for row in range(N):
    i = []
    for col in range(M):
        i.append(arraya[row][col] + arrayb[row][col])
    newarray.append(i)

for row in newarray:
    for col in row:
        print(col, end=' ')
    print()  # 줄 바꿈

