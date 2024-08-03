n,k = map(int,input().split())
inputs = list(map(int,input().split()))


inputs.sort()
inputs.reverse()

print(inputs)
print(inputs[k-1])