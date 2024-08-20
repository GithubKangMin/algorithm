#ldic = {10:[], 11: [],20:[], 21: [], 30:[],31: [], 40:[], 41:[], 50:[], 51:[],60 : [], 61: [] }
result = 0
ldic = {}
n,k = map(int,input().split())
## 딕셔너리 초기화
for i in range(2) :
    for j in range(1,7) :
        ldic[j*10+i] = 0

for _ in range(n):
    s,y = input().split()
    ldic[int(y+s)] = ldic[int(y+s)] + 1

for i in range(1,7):
    for j in range(2):
        if ldic[i*10+j] >= 1:
            if ldic[i*10+j] % k == 0 :
                result += ldic[i*10+j] // k
            else:
                result += (ldic[i*10+j] // k)  + 1
print(result)

