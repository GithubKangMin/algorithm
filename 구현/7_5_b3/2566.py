row=0
col=0

maxnum =0
maxrow =0
maxcol =0
list=[]

for i in range(1, 10):
    row += 1
    a,b,c,d,e,f,g,h,i = map(int,input().split())
    list=[a,b,c,d,e,f,g,h,i]

    if maxnum <=max(list):
        maxnum = max(list)
        maxrow = row
        maxcol = list.index(maxnum)+1


print(maxnum)
print(maxrow, end =" ")
print(maxcol, end ="")

## if maxnum <= max(list) 로 쓴 것과 if maxnum < max(list)가 다른 이유. 모두 0일 때 차이가 남 내가 처음에 모두 0 0 0으로 세팅했기 때문에 모두 0 이면 0 0 나와서 틀리는 것임
## 예시 케이스에서는 최대값 위치 차이지만 0일 때도 포함하려면 =을 넣어주어야 함


