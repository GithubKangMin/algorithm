## input().split()으로 개수 정해놓고 입력값을 받는 것으로 안풀리도록 설계됨 리스트로 받으면 되네  inputValues = list(input().split())

n = int(input())

for _ in range(n):
    inputValues = list(input().split())

    num , values = inputValues[0], inputValues[1:]
    num = float(num)

    for i in values:
        if i=='@':
            num = num * 3
        elif i=='%':
            num = num + 5
        else:
            num = num -7

    print(f"{num:.2f}")