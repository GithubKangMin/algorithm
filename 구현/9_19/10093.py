a,b = map(int,input().split())
if a> b:
    c = a
    a = b
    b = c

l= range(a+1,b)

print(len(l))
print(*l)