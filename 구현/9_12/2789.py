s= input()

c = ["C","A","M","B","R","I","D","G","E"]

for i in s:
    if i in c:
        s = s.replace(i,'')
print(s)