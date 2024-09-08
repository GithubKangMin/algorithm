#문제- 들어오는 사람이 자신이 원하는 번호 말했는데, 그 번호가 이미 차있으면 나가야 함. 거절당한 사람의 수를 구하는 문제
# 문제 풀이 아이디이 - 중복된 숫자 - 1 만큼 거절을 당함 중복된 숫자의 개수 구하는게 아이디어임. 딕셔너리 자료형이 중복을 허가 안하니까 리스트의 길이와 딕셔너리의 길이 비교하면 중복 개수 찾을 수 있을 듯.
## -> 정석 방법이 아닌 것 같은데.. 리스트 + 반복문으로 중복 잡을 수 있을 것 같은데

n=int(input())

values= list(map(int,input().split()))
newList =[]

for i in values[:]:
    if i not in newList:
        newList.append(i)
        values.remove(i)

print(len(values))