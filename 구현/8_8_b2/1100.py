count = 0



for i in range(1,9):
    s= input()
    for j in range(1,9):
        if i % 2 != 0 and j % 2 != 0 and s[j-1] == 'F':
            count += 1
        if i % 2 == 0 and j % 2 == 0 and s[j-1] == 'F':
            count += 1

print(count)