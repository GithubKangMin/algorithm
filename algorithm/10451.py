# 순열 사이클
# 그래프 탐색 dfs
def count_cycles(N,permutation):
    visited = [False] * (N+1)
    count = 0

    for i in range(1, N + 1):
        if not visited[i] : #False 통과
            current = i
            if not visited[i]:
                while not visited[current]: # 사이클 생성되면(True인 노드로 다시 도달) 통과
                    visited[current] = True
                    current = permutation[current]
                count += 1

    return count

T = int(input())
for _ in range(T):
    N = int(input())
    perm = list(map(int,input().split()))
    # index 맞추기 위해 앞에 0추가
    perm = [0] + perm
    print(count_cycles(N,perm))