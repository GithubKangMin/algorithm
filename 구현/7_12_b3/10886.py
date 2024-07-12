p = int(input())

cute=0

for i in range(p):
    opinion = int(input())
    if opinion == 1:
        cute += 1

if p - cute > cute:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")