# 그래프 정의
graph = [
    [],
    [2, 3, 8],  # 노드 1과 연결된 노드들
    [1, 7],     # 노드 2와 연결된 노드들
    [1, 4, 5],  # 노드 3과 연결된 노드들
    [3, 5],     # 노드 4와 연결된 노드들
    [3, 4],     # 노드 5와 연결된 노드들
    [7],        # 노드 6과 연결된 노드들
    [2, 6, 8],  # 노드 7과 연결된 노드들
    [1, 7]      # 노드 8과 연결된 노드들
]

# 방문 여부 정의
visited = [False] * 9

def dfs(graph, v, visited):
    # 현재 노드를 방문처리
    visited[v] = True
    print(v, end= " ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i , visited)

dfs(graph,1,visited)