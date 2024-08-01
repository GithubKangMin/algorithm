## 분수찾기 패턴 찾음 하나 낮추고 하나 올리는 식임 지그재그에서는 시작은 오른쪽만 올리고 번갈아서 올림
# 1,2,3,4,5 마다 주기적으로 바꾸기
#
# numerator = 0
# denominator = 0
#
# frac = [numerator, denominator]
#
# list=[]
#
# n= int(input())
#
#
# l = range(n) # 몇번째 이동인지 체크
#
# for i in l: # i== 몇번째 이동인지 체크하는 리스트의 요소
#     if i % 2 ==0:
#         numerator += 1
#         list.append(f"{numerator}/{denominator}")
#
#     else:
#         denominator += 1
#         list.append(f"{numerator}/{denominator}")
#
#     for j in range(i+1):
#         if i % 2 ==0:
#             denominator += 1
#             list.append(f"{numerator}/{denominator}")
#
#         else:
#             numerator += 1
#             list.append(f"{numerator}/{denominator}")
#
# print(list[n])

# 첫 번째 코드
num = int(input())
line = 1

while num > line:
    num -= line
    line += 1

# 짝수일 경우
if line % 2 == 0:
    a = num
    b = line - num + 1

# 홀수일 경우
else:
    a = line - num + 1
    b = num

print(f'{a}/{b}')

# 두 번째 코드
n = int(input())

# 초기 분수 설정
numerator = 1
denominator = 1

fractions = []

for line in range(1, n + 1):
    for num in range(1, line + 1):
        if line % 2 == 0:
            numerator = num
            denominator = line - num + 1
        else:
            numerator = line - num + 1
            denominator = num

        fractions.append(f"{numerator}/{denominator}")

print(fractions[n - 1])

