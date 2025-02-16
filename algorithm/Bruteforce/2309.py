# 일곱난쟁이

# 9난쟁이중 7난쟁이 찾기

# 9난쟁이의 키 정의

height = []

for i in range(9):
    n = int(input())
    height.append(n)
height.sort()

total = sum(height)

found = False # 정답을 찾았는지 여부 체크 -> 브루트포스에서는 반복문 중첩되므로 필요한 로직

for i in range(9):
    for j in range(i+1,9):
        if total - height[i] - height[j] == 100:
            del_idx1, del_idx2 = j, i  # 삭제할 인덱스 저장
            found = True
            break
    if found:
        break

# 리스트에서 먼저 큰 인덱스를 삭제
del height[del_idx1]
del height[del_idx2]

for i in range(7):
    print(height[i])