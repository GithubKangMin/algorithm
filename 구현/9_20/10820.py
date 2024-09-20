
while(True):
    try:
        s=input()
        result = [0, 0, 0, 0]

        for i in s:
            if not i.isdigit():
                if i.islower():
                    result[0] += 1
                elif i.isupper():
                    result[1] += 1
                else:
                    result[3] += 1
            else:
                result[2] +=1
        print(*result)
    except EOFError :
        break

