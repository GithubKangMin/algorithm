# 체스판 정의
chessboard = [[0 for _ in range(8)] for _ in range(8)]  # 8x8 크기의 체스판

# 현재 나이트의 위치 입력받기
input_data = input("나이트의 위치를 입력하세요 (예: d4): ")
row = int(input_data[1])  # 숫자 좌표
column = int(ord(input_data[0])) - int(ord('a')) + 1  # 문자 좌표를 숫자로 변환

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 이동 가능한 경우의 수 계산
result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]

    # 이동 가능한지 확인 (체스판의 범위 내인지)
    if 1 <= next_row <= 8 and 1 <= next_column <= 8:
        result += 1

print(f"나이트가 이동할 수 있는 경우의 수: {result}")