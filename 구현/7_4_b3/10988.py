#기러기토마토우영우

s = input()

check = True

for i in range(len(s)):
    # if len(s) == 1:
        # break
    if len(s) % 2 ==0:
        if s[i] == s[-i-1]:
            check = True
        else:
            check = False
            break
    else:
        if i == s[int(len(s)/2)+1]:
            break
        if s[i] == s[-i-1]:
            check = True
        else:
            check = False
            break

if check == False:
    print(0)
else:
    print(1)
#
# ## 개선
# s = input()
#
# check = True
#
# for i in range(len(s) // 2):
#     if s[i] != s[-i-1]:
#         check = False
#         break
#
# if check:
#     print(1)
# else:
#     print(0)
#
#
#
# #에러 : False가 나왔는데 break를 안해주면 하나라도 대칭적으로 같은 문자가 생기면 true로 바뀔 수 있다. ture는 빡세게 검열해야 하지만 False는 하나만 틀려도 틀린 것임
#
#
# word = list(str(input()))
#
# if list(reversed(word)) == word:
#     print(1)
# else:
#     print(0)
#
#
# word = input()
# for i in range(len(word)) :
#     if word[i] == word[-1-i] :
#         pass
#     else :
#         print(0)
#         exit(0)
# print(1)
#
#
#
# word = list(input())
# if word == word[::-1] :
#     print(1)
# else :
#     print(0)