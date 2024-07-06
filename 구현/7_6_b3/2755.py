n = int(input())

thak=0
totalscore=0

def new_round(n):
    # 소수점 둘째 자리까지 반올림하기 위해 100을 곱합니다.
    n *= 100

    # n의 소수 부분과 정수 부분을 구합니다.
    integer_part = int(n)
    fractional_part = n - integer_part

    # 소수 부분이 0.5 이상인 경우 정수 부분에 1을 더해줍니다.
    if fractional_part >= 0.5:
        rounded_value = integer_part + 1
    else:
        rounded_value = integer_part

    # 다시 100으로 나누어 소수점 둘째 자리로 변환합니다.
    return rounded_value / 100


score = {'A+':4.3, 'A0':4.0, 'A-':3.7,
         'B+':3.3, 'B0':3.0, 'B-':2.7,
        'C+':2.3,'C0':2.0,'C-':1.7,
        'D+':1.3, 'D0':1.0, 'D-':0.7,
        'F':0.0}

for i in range(n):
    a,b,c= input().split()
    thak += int(b)
    totalscore += float(b)*score[c]

# print(f"{totalscore/thak:.2f}")
print('{0:.2f}'.format(new_round(totalscore/thak)))