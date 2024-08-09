n,m = map(int,input().split())

l =[]

for i in range(1,n+1):
    l.append(i)

for _ in range(m):
    i,j = map(int,input().split())
    l[i-1:j] = reversed(l[i-1:j])
    # l[i-1:j] = l[i-1:j][::-1]

for i in l:
    print(i, end = " ")


