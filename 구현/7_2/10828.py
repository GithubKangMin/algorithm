stack =[]
def push(stack,x):
    stack.append(x)

def pop():
    check = empty()
    if check == 1:
        return -1
    else:
        r= stack[-1]
        stack.pop()
        return r

def size():
    return len(stack)

def empty():
    if len(stack) == 0:
        return 1
    else:
        return 0

def top():
    check = empty()
    if check == 1:
        return -1
    else:
        return stack[-1]

N= int(input())

for i in range(N):
    inputs = input().split()
    if inputs[0] == 'push':
        inputs[1]=int(inputs[1])
        push(stack,inputs[1])
    elif inputs[0] == 'pop':
        print(pop())
    elif inputs[0] == 'size':
        print(size())
    elif inputs[0] == 'empty':
        e = empty()
        if e == 1:
            print(1)
        else:
            print(0)
    elif inputs[0] == 'top':
        print(top())