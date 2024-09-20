colors = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
result=""

for i in range(1, 3):
    c = input()  # 색상 입력받음
    result += str(colors.index(c))  # 색상의 인덱스를 문자열로 추가



c= input()
result=int(result)
result *= 10**colors.index(c)


print(result)


# colors = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
# result = ""
#
# # 첫 두 색상 처리
# for i in range(1, 3):
#     c = input()  # 색상 입력받음
#     result += str(colors.index(c))  # 색상의 인덱스를 문자열로 추가
#
# # 세 번째 색상 처리
# c = input()  # 세 번째 색상 입력받음
# multiplier = 10 ** colors.index(c)  # 세 번째 색상의 승수 계산
#
# # 결과 계산
# result = int(result) * multiplier
#
# print(result)
