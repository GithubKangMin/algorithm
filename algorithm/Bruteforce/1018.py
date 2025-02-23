# 체스판 다시 칠하기
row, col = map(int,input().split())
count = 0
color = ['B','W']
colcheck = 0


for i in range(row):
    string = input()
    check = 0
    temp = 0
    for j in string:
        if check == 0:
            check += 1
            if i == 0:
                colcheck = j
            temp = j
            continue
        if temp == j:
            count += 1
            #temp 값을 이전 값과 다른 값으로 바꿔줘야 됨
            #if 문으로 케이스 나누면 되나
            if j == 'W':
                temp = 'B'
            else:
                temp = 'W'
            continue
        else:
            temp = j
            continue

print(count)

# -> 이 코드는 그냥 매 행마다 bw가 반복되도록 해주는 코드
# 이차원 배열로 정의해서 풀거나 세로 관련된 조건도 정의해줘야 됨
row, col = map(int, input().split())
board = [input() for _ in range(row)]

# 체스판의 색깔 패턴 2가지 정의
chess1 = ["BW" * 4 if i % 2 == 0 else "WB" * 4 for i in range(8)]
chess2 = ["WB" * 4 if i % 2 == 0 else "BW" * 4 for i in range(8)]

min_count = float('inf')

# 모든 8x8 부분 체스판 탐색
for i in range(row - 7):
    for j in range(col - 7):
        count1, count2 = 0, 0  # chess1, chess2와 비교한 색칠 횟수

        for x in range(8):
            for y in range(8):
                if board[i + x][j + y] != chess1[x][y]:
                    count1 += 1
                if board[i + x][j + y] != chess2[x][y]:
                    count2 += 1

        min_count = min(min_count, count1, count2)

print(min_count)


