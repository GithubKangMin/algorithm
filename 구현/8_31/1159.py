## 문제구조 : 일단 성의 맨 첫번째 글자를 하나의 항목으로 추가한 후 생길 때마다 숫자 카운트를 올려줘야 됨 --> 딕셔너리로 처리하는게 좋을 것 같음.
## 문제 풀이 설계 : 결과값 - 사전순으로 공백없이 출력해야 됨 // 첫번째 글자를 떼어와서(인덱스) 딕셔너리의 Key 값으로 넣기. 그리고 앞으로 또 나올 때마다 value 올리기 value값이 5보다 작으면 항복

n = int(input())

dic = {}

result = ''

# 없으면 추가하고 있으면 하나 올려 그거 N 번 반복
for _ in range(n):
    name = input()
    if name[0] not in dic:
        dic[f'{name[0]}'] = 1
    elif name[0] in dic:
        dic[f'{name[0]}'] += 1

# 이제 만들어진 딕셔너리에 value가 5가 넘는 key 값이 있으면 공백없이 출력  ---> 문자열 추가하는 방법

for i in sorted(dic):
    if dic[i] >= 5:
        result += i

## 결과 출력
if len(result) > 0:
    print(result)
else:
    print("PREDAJA")