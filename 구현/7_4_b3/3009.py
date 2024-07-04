#마지막 점 찾기



a,b= map(int,input().split())
c,d= map(int,input().split())
e,f= map(int,input().split())

x=[a,c,e]
y=[b,d,f]

result=[]
xtmp = x[0]
xans = 0
xCheck = False
for i in range(1,3):
    if(x[i] == xtmp) :
        xCheck = True


for i in range(3):
    if b == d:
        result.append(f)
        break

    elif b == f:
        result.append(d)
        break

    elif d == f:
        result.append(b)
        break


for i in result:
    print(i ,end= " ")