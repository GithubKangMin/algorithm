s = input()

cnt=0

temp =""


for i in s:
    temp += i
    cnt+=1
    if cnt %10 ==0:
        print(temp)
        temp =""

if temp:
    print(temp)