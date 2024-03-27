# [ 백준 : 14503번] 로봇청소기
from collections import deque

# 방의 크기
n, m = map(int, input().split())

# (r, c) : 칸의 좌표, d(0:북, 1:동, 2: 남, 3: 서) : 로봇 청소기가 바라보는 방향
r, c, d = map(int, input().split())

# 0 : 빈칸, 1 : 벽, 2 : 청소
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

# 북, 동, 남, 서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(x, y, d):
    queue = deque()
    queue.append((x,y,d))
    graph[x][y] = 2 # 방문; 현재 칸 청소
    count = 1 # 청소 칸 개수

    while queue:
        x, y, d = queue.popleft()
        temp_d = d
        turn = 0
        for i in range(4):
            # 반시계 방향으로 90'회전
            nd = (temp_d + 3) % 4
            nx = x + dx[nd]
            ny = y + dy[nd]
            temp_d = nd # 회전한 방향으로 업데이트

            if 0 <= nx < n and 0 <= ny < m:
                # 청소되지 않은 빈 칸이 있는 경우
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 2 # 방문; 현재 칸 청소
                    queue.append((nx,ny,nd))
                    count += 1
                    break
                # 벽이거나 청소된 경우
                else:
                    turn += 1
        # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
        if turn == 4:
            # 한 칸 후진
            bx = x + dx[(d+2)%4]
            by = y + dy[(d+2)%4]
            # 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춤
            if graph[bx][by] == 1:
                return count
            queue.append((bx,by,d))

print(bfs(r,c,d))
