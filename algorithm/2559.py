N, K = map(int,input().split())

seq = list(map(int,input().split()))
result = 0
l=0

for i in range(N-K+1):
    if sum(seq[i:i+K]) > l :
        result = sum(seq[i:i+K])
    l = sum(seq[i:i + K])
print(result)
# 시간초과


N, K = map(int,input().split())

seq = list(map(int,input().split()))

summ = sum(seq[:K])
maxSum = summ

for i in range(K,N):
    summ += seq[i] - seq[i-K]
    maxSum = max(maxSum, summ)

print(maxSum)