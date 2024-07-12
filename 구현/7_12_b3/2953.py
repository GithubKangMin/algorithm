winnersocre = 0
winner=0
for i in range(1,6):
    a,b,c,d = map(int,input().split())
    score = a+b+c+d
    if score > winnersocre:
        winnersocre = score
        winner = i

print(winner, end = " ")
print(winnersocre)