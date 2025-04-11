def countTile(n):
    na = 15746
    fibo = [0] * (n+2)
    fibo[1] = 1
    fibo[2] = 2

    for i in range(3, n+1):
        fibo[i] = (fibo[i-1] + fibo[i-2]) % na

    return fibo[n]

n= int(input())
print(countTile(n))