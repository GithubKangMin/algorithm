L =int(input())

s= input()

hap = 0

a=0

for i in s:
    hap += (ord(i) -ord('a')+1 )*(31**a)
    a += 1
print(hap%1234567891)