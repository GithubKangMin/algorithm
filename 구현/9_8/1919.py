## 애너그렘 - 철자를 임의로 조합해서 같아질 수 있는 두 문자열 사이의 관계를 칭하는 말
## 문제풀이 --> 입력값을 리스트에 받아서 리스트 길이만큼 반복 순회시키되 순회되는 리스트에서 요소를 하나씩 빼기

l1 = list(input())
l2 = list(input())
result = []
r=0

for i in l1[:]:
    if i in l2:
        result.append(i)
        l1.remove(i)
        l2.remove(i)

print(len(l1)+len(l2))