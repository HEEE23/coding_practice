# [백준 : 5014번] 스타트링크
# bfs 함수 이용
from collections import deque

F, S, G, U, D = map(int, input().split())

visited = [ 0 for i in range(F+1)]
def bfs():
    queue = deque()
    queue.append(S)

    while queue:
        popV = queue.popleft()

        if popV == G:
            print(visited[popV])
            break

        # 현재 노드에서 +U 또는 -D에서 탐색
        for nextS in (popV+U, popV-D):
            # U, G가 0이면 무시
            if nextS == popV:
                continue
            # 엘리베이터가 이동할 수 있고 아직 방문하지 않았다면 버튼의 수 + 1
            if 1 <= nextS <= F and not visited[nextS]:
                visited[nextS] = visited[popV] + 1
                queue.append(nextS)
    else:
        # 엘리베이터로 이동할 수 없을 때
        print("use the stairs")
bfs()
