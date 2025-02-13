N = 0
S = int(input())
a = 1
hap = 0

while(True):
    if hap == S:
        break
    hap += a
    if (S-hap) <= a:
        hap -= a
        N += 1
        break
    N +=1
    a +=1

print(N)