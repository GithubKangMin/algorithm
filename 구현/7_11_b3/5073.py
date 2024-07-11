s = {}

while True:
    a,b,c = map(int,input().split())

    if a==0 and b== 0 and c==0: ## 이거 위치에 따라 런타임 오류가 생길 수도 안 생길 수도 있다.
        break

    l = [a,b,c]
    l = sorted(l)
    if l[2] >= l[0]+l[1]:
        print("Invalid")
        continue


    s = {a,b,c}

    if len(s) == 1:
        print("Equilateral")
    if len(s) == 2:
        print("Isosceles")
    if len(s) == 3:
        print("Scalene")

