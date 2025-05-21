import sys

N, M = map(int, sys.stdin.readline().split())
words = []

# 리스트로 받기
for _ in range(N):
    words.append(sys.stdin.readline().rstrip())

# 빈도수 세기(딕셔너리)
freq= {}
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

# 후보 제거
candidates = []
for word in freq:
    if len(word) >= M:
        candidates.append(word)

# 정렬
def custom_sort(word):
    return (-freq[word], -len(word), word)

candidates.sort(key = custom_sort)

sys.stdout.write('\n'.join(candidates))
