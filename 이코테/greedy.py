# # 그리디 알고리즘
#
# # 1
#
#
# # ------------------
# # 2. 1이 될 때까지
# # 문제 그대로를 구현한 직관적인 풀이
# N = int(input())
# K = int(input())
# count =0
#
# while N>1:
#     if N % K ==0:
#         N = N // K
#         count += 1
#     else:
#         N -= 1
#         count += 1
#
# print(count)
#
# # 시간 효율성을 위해 스킬적으로 풀어낸 풀이 -> 가능하면 시간복잡도 줄이도록 연산 최소화하는 풀이 쓰는게 좋음.
# n, k = map(int, input().split())  # n=17, k=4 입력
# result = 0  # 연산 횟수 초기화
#
# while True:
#     # n이 k로 나누어 떨어지는 가장 가까운 수(target) 찾기
#     target = (n // k) * k  # 몫 * 연산자를 해서 가장 가까운 딱 떨어지는 수를 선제적으로 구함
#     result += (n - target)  # n을 선제적으로 구한 target까지 만드는 연산 횟수를 더함 - 결과처리
#     n = target  # n을 target으로 업데이트
#
#     # n이 k보다 작아지면 종료
#     if n < k:
#         break
#
#     # k로 나누기
#     result += 1
#     n //= k
#
# # 마지막으로 남은 1이 될 때까지 빼기
# result += (n - 1)
# print(result)

# --------
# 3. 곱하기 혹은 더하기 최대한 많이 곱하면 좋은듯?

S = input()
result = 1

for i in S:
    if i == '0':
        pass
    else:
        result *= int(i)

print(result)


# 0001 일 때도 정확히 답 냄
data = input()

result = int(data[0])  # 첫 번째 숫자부터 시작

for i in range(1, len(data)):
    num = int(data[i])  # 현재 숫자
    if num <= 1 or result <= 1:  # 현재 숫자나 결과가 0 또는 1인 경우 더하기
        result += num
    else:  # 그 외에는 곱하기
        result *= num

print(result)

