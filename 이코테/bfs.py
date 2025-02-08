from collections import deque
# dfs

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

visited = [False] * 9

def bfs(graph, start, visited):
    queue = deque([start])  # 시작 노드를 큐에 넣음
    visited[start] = True   # 시작 노드를 방문 처리

    while queue:  # 큐가 빌 때까지 반복
        v = queue.popleft()  # 큐에서 노드를 하나 꺼냄
        print(v, end=' ')    # 방문한 노드 출력

        for i in graph[v]:  # 현재 노드와 연결된 모든 노드 확인
            if not visited[i]:  # 방문하지 않은 노드라면
                queue.append(i)  # 큐에 추가
                visited[i] = True  # 방문 처리


bfs(graph, 1, visited)