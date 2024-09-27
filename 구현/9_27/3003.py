n=[1,1,2,2,2,8]

vals=list(map(int,input().split()))

for i in range(6):
    n[i] = n[i] - vals[i]

print(*n)