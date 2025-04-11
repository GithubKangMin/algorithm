N = int(input())

# 입력받은 학생들을 [5,4,1,3,2]의 리스트 형태로 바꿔준다.
students = list(map(int, input().split()))

stack = []

now_turn = 1
for student in students:
	# 대기열 -> 임시 대기 공간
    stack.append(student)
    # 스택이 비어있지 않고, 스택의 마지막 학생(맨 위 학생)이 지금 나가야 할 학생이라면
    while stack and stack[-1] == now_turn:
        stack.pop() # 차례 학생이라면 스택에서 빼고
        now_turn +=1 # 다음 차례로 저장한다.

# 반복문을 전부 돌았는데 스택에 요소가 남았다면 더 이상 진행이 불가능한 것이므로
if stack:
    print('Sad')
else:
    print('Nice')

    # while문 = if문 조건 만족하지 않을 때까지 반복
    #
    # if 조건
    #   while조건
    # 걸어도 if가 필요 없음
