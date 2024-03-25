# [백준 : 2178번] 미로 탐색
# bfs 함수 이용
from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 상, 하, 좌, 후
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    # queue가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            # 위치를 벗어나면 무시
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            # 0은 이동할 수 없는 칸으로 무시
            if graph[nx][ny] == 0:
                continue
            # 1이면 이동할 수 있는 칸으로 최소 칸 수+1
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # (n, m) 위치일 때 최소 칸 수
    return graph[n-1][m-1]

print(bfs(0,0))
