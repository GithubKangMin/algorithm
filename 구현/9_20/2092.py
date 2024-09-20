s= input()

result =""
cap=False

for i in s:
    if result == "":
        result += i
    else:
        if i == "-":
            cap =True
            continue
        if cap == True:
            result += i
            cap = False
print(result)