# 수리공 항승 실버 3

# 입력값 받기 : 테이프 길이랑 구멍 개수 정의
N , L = map(int,input().split())

# 입력값 리스트로 해서 오름차순 정렬하기 : 구멍 위치, 필요 테입 개수 정의
hole = []
hole = list(map(int,input().split()))
hole.sort()
tape = 0
temp = 0

# L-만큼 차이나는 숫자 모임이 있으면 한번에 커버
for i in hole:
    # 첫 루프 패스
    if i == hole[0]:
        temp = i
        continue

    if L - 1 == i - temp:
        tape += 1
        continue

    elif L - 1 > i- temp:
        continue

    else:
        tape += 1
        temp = i
        continue
print(tape)



# ------
# 수리공 항승 실버 3

# 입력값 받기
N, L = map(int, input().split())

# 구멍 위치 정렬
hole = sorted(map(int, input().split()))

tape = 1  # ✅ 첫 번째 테이프는 무조건 필요
temp = hole[0]  # ✅ 첫 번째 구멍부터 시작

# L-1 이하의 간격도 하나의 테이프로 커버 가능하도록 수정
for i in hole:
    if i - temp >= L:  # ✅ 테이프 길이를 초과하면 새로운 테이프 사용
        tape += 1
        temp = i  # ✅ 새로운 테이프 시작점 업데이트

print(tape)



