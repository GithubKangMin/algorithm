N = int(input())

# last = [0]
# newLast= []
#
# # 마지막자리만
# for _ in range(1, N-1):
#     newLast = []
#     for i in last:
#         if i == 0:
#             newLast.append(0)
#             newLast.append(1)
#         else:
#             newLast.append(0)
#         last = newLast
#
# print(len(last))


zero_count = 1
one_count = 0

for _ in range(1, N-1):
    new_zero = zero_count + one_count  # 0에서 0,1 나오니까 0 추가 1 추가 → 전부 0으로 세면 됨
    new_one = zero_count

    zero_count = new_zero
    one_count = new_one

print(zero_count + one_count)  # 전체 길이 = 0의 개수 + 1의 개수