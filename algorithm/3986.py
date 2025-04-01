def isGoodWord(word):
    stack = []

    for char in word:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return len(stack) == 0

n = int(input())
result = 0

for _ in range(n):
    word = input()
    if isGoodWord(word):
        result += 1

print(result)