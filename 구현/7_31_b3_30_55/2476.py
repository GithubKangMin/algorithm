n = int(input())
totalsang = 0
sang=0

for _ in range(n):
    nun1,nun2,nun3 = map(int,input().split())
    if nun1 == nun2 == nun3:
      sang = 10000 + nun1*1000
    elif nun1 == nun2 or nun1 == nun3 or nun2 == nun3:
        if nun1 == nun2 or nun1 == nun3:
            sang = 1000 + nun1*100
        elif nun2 == nun3:
            sang = 1000 + nun2*100
    elif nun1 != nun2 != nun3:
        sang = max(nun1,nun2,nun3)*100
    if sang > totalsang:
        totalsang = sang

print(totalsang)