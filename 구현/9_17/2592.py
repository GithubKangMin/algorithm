l = []
a = [0]*1001
# 입력값 받기
for _ in range(10):
    n= int(input())
    l.append(n)

# 최빈값 구하기 어떻게 구하지?
for i in l:
    a[i] += 1


# 평균구하기
print(int(sum(l)/10))
print(a.index(max(a)))

