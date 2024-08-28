## 막대기 오른쪽에서 봤을 때 몇개를 볼 수 있는지 -> 막대기 그룹을 리스트로 넣고 오른쪽부터 탐색해서 더 큰게 나오면 바꿔가면서 갱신하고 count를 올린다.
import sys

input = sys.stdin.readline  # input 함수를 sys.stdin.readline으로 덮어쓰기

mak = []
result = 0
max = 0

n= int(input())

# 리스트 만들고 리스트 뒤집기
for _ in range(n):
    m = int(input())
    mak.append(m)

mak.reverse()

#최대값 갱신하는 논리
for i in mak:
    if i >max :
        max = i
        result +=1

print(result)