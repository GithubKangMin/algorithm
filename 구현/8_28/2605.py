#풀이 방법 1. 첫 리스트 만들지 말고 처음부터 맨 뒤에 있는 학생이 몇칸 씩 움직이면서 추가되도록 설계 2. 첫 리스트 만든 뒤에 배정받는 수대로 움직이게 만들기

n = int(input())
l=[]


# 일단 1부터 입력된 수까지 정상적인 리스트 만들기
# for i in range(1,n+1):
#     l.append(i)

# 값들을 입력받아서 각 학생이 앞으로 몇 칸 움직일지 배정하고 그대로 리스트 수정하기
values = list(map(int,input().split()))
i=1
for j in values:
        l.insert(len(l)-j,i)   ## 리스트의 특정 자리에 append 메서드를 쓸 수 있는 건가? 기본적으로 append 함수가 그냥 맨 뒤에 추가하는 메서드잖아 맞네 원하는 자리에 요소 추가하고 싶으면 Insert()메서드 써야 됨
        i+=1

for i in l:
    print(i, end = " ")