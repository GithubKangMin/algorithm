n = int(input())
vals=list(map(int,input().split()))
M=max(vals)
a=0
for i in vals:
    vals[a]= i/M*100
    a+=1
print(sum(vals)/n)