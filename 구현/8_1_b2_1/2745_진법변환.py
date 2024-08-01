N , B = input().split()
B=int(B)

resultList = list(N)[::-1]

result=0

for i in range(len(resultList)):
    if resultList[i].isdigit():

        result += int(resultList[i])*(B**i)
    else:
        result += (ord(resultList[i]) - 55) * (B ** i)

print(result)
