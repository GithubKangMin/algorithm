n = int(input())

values= sorted(list(map(int,input().split())))

print(values[-1]- values[0])