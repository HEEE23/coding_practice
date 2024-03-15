# [백준 : 2667번] 단지번호붙이기
# bfs 이용
from collections import deque

n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 상, 하, 좌, 우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0
    count = 1
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            # 지도 범위에 벗어나게 되면 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            # 0은 집이 없는 곳
            if graph[nx][ny] == 0:
                continue
            # 1은 집이 있는 곳으로 단지에 속하는 집의 수 계산
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx,ny))
                count += 1
    return count

# 단지에 속하는 집의 수를 넣기 위한 변수
cnt = []

# 지도 모든 위치에 대하여 단지 내 집의 수 확인
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt.append(bfs(i, j))

# 오름차순 정렬
cnt.sort()

print(len(cnt)) # 총 단지 수

# 각 단지내 집의 수
for i in range(len(cnt)):
    print(cnt[i])