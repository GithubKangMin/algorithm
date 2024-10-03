arr =[
    [],
    [],
    [],
    [],
    []
]
for i in range(5):
    arr[i] = list(input())

result = ""
M=0

for row in arr:
    if len(row) > M:
        M = len(row)


# for i in range(5):
#     for j in range(M):
#         if j < len(arr[i]):
#             result += arr[i][j]

##열이 fix 행을 움직여야 됨 -> i 가 열
# for i in range(5):
#     for j in range(M):
#         if j < len(arr[i]):
#             result += arr[i][j]
# -> 행을 고정하고 열을 순회하는 코드를 짰네

for i in range(M):
    for j in range(5):
        if i < len(arr[j]):
            result += arr[j][i]

print(result)

#
# arr = [
#     [],
#     [],
#     [],
#     [],
#     []
# ]
#
# # 2차원 배열에 사용자 입력 받기
# for i in range(5):
#     arr[i] = list(input())  # 공백 없이 입력된 각 문자를 리스트로 저장
#
# result = ""
# M = 0
#
# # 가장 긴 행의 길이 찾기
# for row in arr:
#     if len(row) > M:
#         M = len(row)
#
# # 열을 기준으로 행을 순회 (세로로 읽기)
# for i in range(M):  # 열을 고정
#     for j in range(5):  # 각 행을 순회
#         # 현재 열이 행의 길이보다 작은 경우에만 값을 추가
#         if i < len(arr[j]):
#             result += arr[j][i]
#
# print(result)