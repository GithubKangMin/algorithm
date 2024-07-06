#마지막 점 찾기



a,b= map(int,input().split())
c,d= map(int,input().split())
e,f= map(int,input().split())

x=[a,c,e]
y=[b,d,f]

result=[]

for i in range(3):
    if a == c:
        result.append(e)
        break
    elif a == e:
        result.append(c)
        break

    elif c == e:
        result.append(a)
        break


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



## 다른 풀이
x_nums = []
y_nums = []
for _ in range(3):
    x, y = map(int, input().split())
    x_nums.append(x)
    y_nums.append(y)

#한개인 요소를 찾아서 출력하는 것 count 함수 이용하기
for i in range(3):
    if x_nums.count(x_nums[i]) == 1:
        x4 = x_nums[i]
    if y_nums.count(y_nums[i]) == 1:
        y4 = y_nums[i]
print(x4, y4)