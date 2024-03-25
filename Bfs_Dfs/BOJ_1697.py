# [백준 : 1697번] 숨바꼭질
# bfs
from collections import deque
n, k = map(int, input().split())

MAX = 10**5
dist = [0]*(MAX+1)
def bfs():
    queue = deque()
    queue.append(n)

    while queue:
        popV = queue.popleft()

        if popV == k:
            print(dist[popV])
            break

        for nextN in (popV+1, popV-1, 2*popV):
            if 0<=nextN<=MAX and not dist[nextN]:
                dist[nextN] = dist[popV] + 1
                queue.append(nextN)

bfs()
