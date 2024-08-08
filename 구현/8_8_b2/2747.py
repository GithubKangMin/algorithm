## 피보나치 수열
# 재귀함수로 구현하기 --> 시간초과
# def fibo(n):
#     if n == 1:
#         return 1
#     if n == 0:
#         return 0
#     return fibo(n-1)+ fibo(n-2)
#
# a= int(input())
# print(fibo(a))

## for문으로 구현하기

fibo = [0,1]

n= int(input())

for i in range(n):
    hap = fibo[i] + fibo[i+1]
    fibo.append(hap)


print(fibo[n])