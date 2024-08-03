# 반복문 이용한 풀이
# n = int(input())
#
# fibo = [0,1]
#
# for i in range(n):
#     if n>=2 and len(fibo) <= n:
#         fibo.append(i)
#


memo = [0, 1]
n = int(input())

if n >= 2:
    for i in range(2, n + 1):
        memo.append(memo[-1] + memo[-2])

print(memo[n])


# 재귀함수를 이용한 풀이
# def fibo(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     return fibo(n-1) + fibo(n-2)
#
# n= int(input())
# print(fibo(n))

# 중간에 값을 저장하는 배열을 이용하는 계산: 이러면 출력시간이 줄어듦
# def fibo2(n):
#     global memo
#     메모 리스트 채우는 if 문
#     if n>=2 and len(memo) <=n:
#         memo.append(fibo2(n-1) + fibo2(n-2)) ## 3 넣으면 2까지 한번에 추가한 뒤에 3을 추가한다.
#     return memo[n]
#
# memo = [0,1]
# n = int(input())
# print(fibo2(n))
