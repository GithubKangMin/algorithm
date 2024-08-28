n = int(input())
l=[]
#
# for i in range(1,n+1):
#     l.append(i)

values = list(map(int,input().split()))
i=1
for j in values:
        l.append(i)
        i+=1

print(l)
