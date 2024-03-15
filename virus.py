# [백준 : 2606번] 바이러스
# bfs함수 사용
from collections import deque

n = int(input()) # 컴퓨터의 수
m = int(input()) # 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수

adj_matrix = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    start, end = map(int, input().split())
    adj_matrix[start][end] = 1
    adj_matrix[end][start] = 1

visited = [False]*(n+1)

def bfs(v):
    queue = deque([v])
    visited[v] = True
    count = 0 # 연결되어 있는 컴퓨터의 수를 구하기 위한 변수

    # queue가 빌 때까지
    while queue:
        pop = queue.popleft()

        for i in range(n+1):
            if adj_matrix[pop][i] == 1 and not visited[i]:
                queue.append(i)
                count += 1
                visited[i] = True
    return count

# 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수
print(bfs(1))