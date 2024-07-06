# ## if문으로 넣으면 쉽게 풀릴 것 같지만 다른 규칙
#
# s = input()
#
#
# if s[0] == 'A':
#     score =4.0
# elif s[0] == 'B':
#     score =3.0
# elif s[0] == 'C':
#     score =2.0
# elif s[0] == 'D':
#     score =1.0
# elif s[0] == 'F':
#     score =0.0
#
#
# try:
#     if s[1] == '+':
#         score += 0.3
#     elif s[1] == '-':
#         score -= 0.3
# except IndexError:
#     pass
#
# print(score)

##딕셔너리로 푸는게 더 깔끔한 듯

score = {'A+':4.3, 'A0':4.0, 'A-':3.7,
         'B+':3.3, 'B0':3.0, 'B-':2.7,
        'C+':2.3,'C0':2.0,'C-':1.7,
        'D+':1.3, 'D0':1.0, 'D-':0.7,
        'F':0.0}

inputScore = input()
print(float(score[inputScore]))
