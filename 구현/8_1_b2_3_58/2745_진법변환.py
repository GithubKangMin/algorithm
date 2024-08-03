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


## isdigit()메서드 숫자면 true 아니면 false .으로 접근

#다른 풀이- int 메서드가 임의의 진법의 수를 10진법으로 변환하는데에도 쓰인다.
# n, b = input().split()
# print(int(n, int(b)))
