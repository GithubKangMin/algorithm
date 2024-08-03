# n = int(input())
#
# for _ in range(n):
#     a,b = map(int,input().split())
#     lastDigit = (a**b) %10
#     print(lastDigit)
## ->시간초과

n = int(input())

for _ in range(n):
    a,b = map(int,input().split())
    l=a
    for i in range(b):
        s=str(l*a)
        l= s[-1]
        if i == b-1:
            print(l)

# n = int(input())
#
# for _ in range(n):
#     a, b = map(int, input().split())
#     l = a
#     for i in range(b):
#         s = str(l * a)
#         l = int(s[-1])
#     print(l)