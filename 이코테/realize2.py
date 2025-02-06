# 시각- 완전 탐색

N = int(input())
totalTime = 60 * 60 * (N+1)
result = 0

si = 0
bun = 0
cho = 0

for _ in range(totalTime):
    cho += 1
    # 시간 중 하나라도 3이 들어가 있다면 1 증가
    if '3' in str(si) + str(bun) + str(cho):
        result += 1
    # 시계가 정상적으로 돌아가도록 매 타임 초기화: 이게 큰 단위가 먼저 검사돼야 하네 분을 나중으로 하니까 앞에서 다 걸러버려서 뒤를 체크를 못해준거였네
    if bun == 59 and cho == 59:
        si += 1
        bun = 0
        cho = 0

    if cho == 59:
        cho = 0
        bun += 1

print(result)

# 시각 - 완전 탐색

N = int(input())
totalTime = 60 * 60 * (N+1)
result = 0

si = 0
bun = 0
cho = 0

for _ in range(totalTime):
    cho += 1
    # 시간 중 하나라도 '3'이 포함되어 있다면 1 증가
    if '3' in str(si) + str(bun) + str(cho):
        result += 1
    # 초가 59에 도달하면 초기화
    if cho == 59:
        cho = 0
        bun += 1  # 분 증가 추가
    # 분이 59에 도달하면 시 증가
    if bun == 59:
        si += 1
        bun = 0

print(result)

# H 입력받기
h = int(input())

count = 0
for i in range(h + 1):  # 0시부터 h시까지
    for j in range(60):  # 0분부터 59분까지
        for k in range(60):  # 0초부터 59초까지
            # 매 시간 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)