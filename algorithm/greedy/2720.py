# 5달러

n = int(input()) # 거스름돈 정의
change = [0,0,0,0] # 주는 돈 정의 0.25 0.1 0.05 0.01
count = 0

# 최상단부터 빼는 알고리즘 : 그리디 알고리즘 비효율적인 그리디
for i in range(n):
    money = int(input())
    # 0.25 배율로 뺄 수 있는 최대로 빼세요 - 반복문으로 구현하면 될 것 같은데
    while(money >= 25):
        money -= 25
        count += 1
    change[0] = count
    count = 0
    while(money >= 10):
        money -= 10
        count += 1
    change[1] = count
    count = 0
    while(money >= 5):
        money -= 5
        count += 1
    change[2] = count
    count = 0
    while(money >= 1):
        money -= 1
        count += 1
    change[3] = count
    count = 0
    print(*change)


n = int(input())

for _ in range(n):
	money = int(input())
	for i in [25, 10, 5, 1]:
		print(money//i, end=' ')
		money = money%i

# 반복문 안에 input() 넣으면 깔끔해지는구나
# 개 비효율적으로 풀었구나
# 나누기를 잘 활용하면 깔끔해지는구나 반복문으로 계속 뺄 필요 없이