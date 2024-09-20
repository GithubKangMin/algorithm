# s= input()
# post =""
# result = 0
#
#
# for i in s:
#     if post =="":
#         post = i
#         result += 10
#     else:
#         if post != i:
#             result += 5
#         else:
#             result += 10
#     post = i
#
# print(result)

s = input()
post = ""  # 이전 문자를 저장할 변수
result = 0

for i in s:
    if post == "":  # 첫 번째 문자일 경우
        result += 10
    else:
        if post != i:  # 이전 문자와 다른 경우
            result += 10
        else:  # 이전 문자와 같은 경우
            result += 5
    post = i  # 현재 문자를 post에 저장하여 다음 반복에서 비교

print(result)
