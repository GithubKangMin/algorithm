l= list(range(1,21))

for _ in range(10):
    a,b= map(int,input().split())
    l[a-1:b] = list(reversed(l[a-1:b]))

print(*l)