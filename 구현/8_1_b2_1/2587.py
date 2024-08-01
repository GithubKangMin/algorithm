numlist = []

for i in range(5):
    n=int(input())
    numlist.append(n)

sumnum = sum(numlist)

numlist.sort()

print(int(sumnum/5))
print(numlist[2])