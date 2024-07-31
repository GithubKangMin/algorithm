n = int(input())

print(" " * (n - 1)+ "*")

for i in range(1,n+1):
        # n = n -1
    if i == n :
        print("*"*(2*(n-1)))
        # n = n-1
    else:
        print(" " * (n - 1 - i) + "*" + " " * (2 * i - 1) + "*")