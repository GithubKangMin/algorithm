# 블랙잭
# 브루트포스

# 카드 개수와 목표숫자 정의
N, M = map(int,input().split())

# 정해진 카드 정리해서 정의
card = sorted(list(map(int,input().split())))

# 목표 숫자에 가장 가깝게 닿을 수 있는 경우의 수: 모든 경우의 수 고려 = 브루트 포스

currentmax = 0

# for i in card:
#     for i+1 in card:
#         for i+2 in card:
# -> 브루트포스할 때 리스트 말고 range로 새로 만들어서 계산해야되는구나

for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            total = card[i] + card[j] + card[k]
            if total > currentmax and total <= M:
                currentmax = total

print(currentmax)