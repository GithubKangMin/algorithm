# n = int(input())
#
# for _ in range(n):
#     a,b = map(int,input().split())
#     lastDigit = (a**b) %10
#     print(lastDigit)
## ->시간초과

# n = int(input())
#
# for _ in range(n):
#     a,b = map(int,input().split())
#     l=a
#     for i in range(b):
#         s=str(l*a)
#         l= s[-1]
#         if i == b-1:
#             print(l)

# n = int(input())
#
# for _ in range(n):
#     a, b = map(int, input().split())
#     l = a
#     for i in range(b):
#         s = str(l * a)
#         l = int(s[-1])
#     print(l)


## 끝자리 데이터
sequences = {
    0: [10],
    1: [1],
    2: [2, 4, 8, 6],
    3: [3, 9, 7, 1],
    4: [4, 6],
    5: [5],
    6: [6],
    7: [7, 9, 3, 1],
    8: [8, 4, 2, 6],
    9: [9, 1],
}

T= int(input())


for _ in range(T):
    a, b = map(int,input().split())
    a = a % 10
    print(sequences[a][b%len(sequences[a])-1])

# import sys
# #
# sequences = {
#     1: [1],
#     2: [2, 4, 8, 6],
#     3: [3, 9, 7, 1],
#     4: [4, 6],
#     5: [5],
#     6: [6],
#     7: [7, 9, 3, 1],
#     8: [8, 4, 2, 6],
#     9: [9, 1]
# }
#
# input = sys.stdin.read
# data = input().split()
#
# T = int(data[0])
# index = 1
#
# for _ in range(T):
#     a = int(data[index])
#     b = int(data[index + 1])
#     index += 2
#     print(sequences[a][(b - 1) % len(sequences[a])])


# T = int(input())
#
# for _ in range(T):
#     a, b = map(int, input().split())
#     a = a % 10
#
#     if a == 0:
#         print(10)
#     elif a == 1 or a == 5 or a == 6:
#         print(a)
#     elif a == 4 or a == 9:
#         b = b % 2
#         if b == 1:
#             print(a)
#         else:
#             print((a * a) % 10)
#     else:
#         b = b % 4
#         if b == 0:
#             print((a ** 4) % 10 % 10 % 10)
#         else:
#             print((a ** b) % 10 % 10 % 10)


