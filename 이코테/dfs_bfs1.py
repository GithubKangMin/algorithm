n,m = map(int,input().split())
graph = []

for i in range(n):
    graph.append(list(map(int,input())))

count = 0

def dfs(x,y):
    global count
    #주어진 범위를 벗어나느 경우 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
        # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 1:
        # 해당 노드 방문 처리
        graph[x][y] = 0
        count += 1
        # 상, 하, 좌, 우 위치를 모두 재귀적으로 방문
        dfs(x, y - 1)
        dfs(x + 1, y)
        return True
    return False

print(count)