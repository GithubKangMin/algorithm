# 재귀
# def dfs(graph, v, visited, result):
#     visited[v] = True
#     result.append(v)
#     for i in sorted(graph[v]):
#         if not visited[i]:
#             dfs(graph, v, visited, result)
#
# N , M, start = map(int,input().split())
# graph = [[] for _ in range(N+1)]
#
# for _ in range(M) :
#     u, v = map(int, input().split())
#     graph[u].append(v)
#     graph[v].append(u)
#
# visited = [False] * (N+1)
# result =[]
#
# dfs(graph, start, visited, result)
#
# for node in result:
#     print(node)

def dfs(graph, start):
    visited = [0] *(N+1)
    stack = [start]
    order = 1

    while stack:
        v = stack.pop()
        if visited[v] == 0:
            visited[v] = order
            order += 1
            stack.extend(sorted(graph[v], reverse = True))
    return visited

N , M, start = map(int,input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M) :
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

result =dfs(graph, start)

for i in range(1, N+1):
    print(result[i])



