def find(parent, x) :
    if parent[x] != x:
        parent[x] =find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    root_a = find(parent,a)
    root_b = find(parent,b)
    if root_a != root_b:
        parent[root_b] = root_a
        return True
    return False

T = int(input())
for _ in range(T):
    N, M = map(int,input().split())
    parent = [i for i in range(N+1)]
    count = 0

    for _ in range(M):
        a, b = map(int,input().split())
        if union(parent,a,b):
            count += 1
    print(count)