# 설탕배달 - 거스름 돈이랑 똑같은 것 같은데 좀 더 복잡하네
# 나머지가 일정한 패턴을 가지기 때문에 이를 이용하면 해결할 수 있다고 판단
# 패턴을 잡고 예외를 일일히 처리해주는 하드코딩의 요소가 남아있음.
# 패턴을 활용한 규칙 기반 접근법일 뿐 그리디 알고리즘으로 푼 것은 아님
N = int(input())

# 5를 여러 번 빼서 해결할 수 없는 경우를 먼저 처리
if N in [4, 7]:
    print(-1)

# 5로 나누어떨어지는 경우
elif N % 5 == 0:
    print(N // 5)

# 5로 나누었을 때 나머지가 3이면 3kg 한 개 추가
elif N % 5 == 3:
    print(N // 5 + 1)

# 5로 나누었을 때 나머지가 1이면 5kg 하나 줄이고 3kg 두 개 추가
elif N % 5 == 1:
    print(N // 5 - 1 + 2)

# 5로 나누었을 때 나머지가 4이면 5kg 하나 줄이고 3kg 세 개 추가
elif N % 5 == 4:
    print(N // 5 - 1 + 3)

# 5로 나누었을 때 나머지가 2이면 5kg 두 개 줄이고 3kg 네 개 추가
elif N % 5 == 2:
    print(N // 5 - 2 + 4)

# 3 또는 5만 있는 경우
elif N == 3 or N == 5:
    print(1)

# --------------------------
# 그리디 알고리즘으로 푼 풀이
N = int(input())

count = 0
while N >= 0:
    if N % 5 == 0:  # 5kg으로 정확히 나누어떨어지는 경우
        count += N // 5
        print(count)
        break
    N -= 3  # 5로 나누어떨어질 때까지 3kg씩 빼기
    count += 1
else:
    print(-1)  # 정확한 무게를 만들 수 없는 경우