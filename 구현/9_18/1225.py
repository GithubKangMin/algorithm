# a,b= input().split()
#
# result=0
#
# for i in a:
#     for j in b:
#         result += int(i) * int(j)
#
# print(result)


a,b= input().split()

suma =0
sumb =0

for i in a:
    suma += int(i)
for i in b:
    sumb += int(i)


print(suma * sumb)
