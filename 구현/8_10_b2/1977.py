def wanjeon(n):
    root = int(n ** 0.5)
    if n == root ** 2:
        return n
    return

result = 0

m = int(input())
n = int(input())
mini = 1000000

for i in range(m,n+1):
    if wanjeon(i) == i:
        result += wanjeon(i)
        if wanjeon(i) < mini:
            mini = wanjeon(i)


if result == 0:
    print(-1)
else:
    print(result)
    print(mini)