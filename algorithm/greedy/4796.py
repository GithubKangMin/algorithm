# 그리디 알고리즘
case_num = 1

while(True):
    # 규칙일 l,p와 휴가일 v 정의
    l, p, v = map(int, input().split())
    result = 0
    if l == 0 and p == 0 and v== 0 :
        break
    result += v // p * l
    v %= p
    if v >= l:
        result += l
    else:
        result += v
    print(f"Case {case_num}: {result}")
    case_num += 1