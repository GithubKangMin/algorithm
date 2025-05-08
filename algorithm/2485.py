import sys
import math
input = sys.stdin.readline

N = int(input())
pos = [int(input()) for _ in range(N)]

diff = [pos[i+1] - pos[i] for i in range(N-1)]

#최대공약수
a = diff[0]
for d in diff[1:]:
    a= math.gcd(a,d)


b = (pos[-1] - pos[0]) // a+1

print(b - N)