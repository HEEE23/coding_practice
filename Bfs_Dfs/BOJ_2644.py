# [백준 : 2644번] 촌수계산
# dfs 함수 이용
n = int(input()) # 전체 사람의 수
a, b = map(int, input().split()) # 촌수를 계산해야 하는 서로 다른 두 사람의 번호
m = int(input()) # 부모 자식들 간의 관계의 개수

adj_matrix = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    start, end = map(int, input().split())
    adj_matrix[start][end] = 1
    adj_matrix[end][start] = 1

visited = [False]*(n+1)

result = []
def dfs(a, count):
    stack = []
    stack.append(a)
    visited[a] = True
    count += 1

    # stack이 빌 때까지 반복
    while stack:
        # 출발 노드(a)에서 b가 나타나면, 그 때 count를 결과값에 입력 후 break
        # 촌수를 나타내는 정수
        if a == b:
            result.append(count)
            break
        # b를 발견하지 못했으면, stack이 빌 때까지 반복
        else:
            popV = stack.pop()
            visited[popV] = True

            for i in range(n+1):
                if adj_matrix[popV][i] == 1 and not visited[i]:
                    dfs(i, count) # 재귀함수
    return result

dfs(a, 0)

# 촌수를 계산할 수 없을 때(= result 값이 비었을 때), -1 출력
if len(result) == 0:
    print(-1)
else:
    print(result[0]-1)
