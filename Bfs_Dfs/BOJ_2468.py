# [백준 : 2468번] 안전 영역
# bfs 사용
from collections import deque
n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

high = 0 # 물에 잠기는 높이

# 물에 잠길 수 있는 최대 높이
for i in range(n):
    for j in range(n):
        if graph[i][j] > high:
            high = graph[i][j]

def bfs(x,y, high):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] > high and not visited[nx][ny]:
                queue.append((nx,ny))
                visited[nx][ny] = 1

result = 0
for k in range(high):
    visited = [[0]*n for _ in range(n)]

    cnt = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > k and visited[i][j] == 0:
                bfs(i, j, k)
                cnt += 1
    # 안전한 영역의 최대 개수
    if result < cnt:
        result = cnt

print(result)
