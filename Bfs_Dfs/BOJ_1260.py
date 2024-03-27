# [백준 : 1260번] DFS와 BFS

# n : 정점의 개수, m : 간선의 개수, v : 시작할 정점의 번호
n, m, v = map(int, input().split())

adj_matrix = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    start, end = map(int, input().split())
    adj_matrix[start][end] = 1
    adj_matrix[end][start] = 1

# dfs; 재귀함수 사용
visited_d = [False]*(n+1)

def dfs(v):
    stack = []
    stack.append(v)
    visited_d[v] = True

    while stack:
        pop_d = stack.pop()
        print(pop_d, end=" ")

        for i in range(n+1):
            if adj_matrix[pop_d][i] == 1 and not visited_d[i]:
                dfs(i)

# bfs; deque 이용
from collections import deque

visited_b = [False]*(n+1)
def bfs(v):
    queue = deque([v])
    visited_b[v] = True

    while queue:
        pop_b = queue.popleft()
        print(pop_b, end=" ")

        for i in range(n+1):
            if adj_matrix[pop_b][i] == 1 and not visited_b[i]:
                queue.append(i)
                visited_b[i] = True
dfs(v)
print()
bfs(v)
        
