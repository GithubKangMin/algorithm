train=0
maxPeople=0
#최대값 구하기 매번 갱신하는 방법

for _ in range(4):
    out , on = map(int,input().split())
    train -= out
    train += on
    if train > maxPeople :
        maxPeople = train

print(maxPeople)