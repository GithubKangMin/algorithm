n = int(input())

for _ in range(n):
    m , s = input().split()
    m = int(m)
    s = s[:m-1] + s[m:]
    print(s)

