# A,B,C = map(int,input().split())
#
# result=0
# start =[]
# end = []
#
#
# for _ in range(3):
#     t1, t2 = map(int,input().split())
#     start.append(t1)
#     end.append(t2)
#
# time = range(min(start),max(end)+1)
#
# start.sort()
# end.sort()
#
# result += (time[end[0]-start[2]])*3*C
# time.


# result= (end[0]-start[2])*3*C + (end[1]-start[1]) *2 *B + (end[2]-start[0]) * A
# print(result)


## 구간을 통으로 계산하니까 빈 부분 못빼서 시간이 너무 길어졌네.. 방법이 안떠오르네 리스트로 만들어서 겹치는 부분 할까 근데 그런 방법이 있나??
## 제일 작은 수부터 제일 큰 수까지 리스트를 만든 다음 계산하고 나서 그 구간 버리는 방법
## 리스트 숫자 올려서 숫자할당하기

A,B,C = map(int,input().split())

l=[0]*101


for _ in range(3):
    t1, t2 = map(int,input().split())
    for i in range(t1,t2):
        l[i]+=1

result = l.count(3)*3*C + l.count(2)*2*B + l.count(1)*A

print(result)