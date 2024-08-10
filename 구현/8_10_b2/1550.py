a = input()
result = 0


for i in range(len(a)):
    if a[i].isdigit():
        result += int(a[i]) * 16 ** (len(a) - i - 1)
    else:
        result += (ord(a[i]) - 55) * 16 ** (len(a) - i - 1)
print(result)