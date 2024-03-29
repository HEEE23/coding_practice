# [백준 : 1149번] RGB거리
# DP
n = int(input()) # 집의 수
rgb = [list(map(int, input().split())) for _ in range(n)] # 각집을 R, G, B로 칠하는 비용
d = [[0]*3 for _ in range(n)]

d[0] = rgb[0]

# 누적합 이용
# 현재 집에 칠한 색을 제외했을 때, 이전 집에서 칠할 수 있는 색의 비용 중 최솟값
for i in range(1,n):
    d[i][0] = min(d[i-1][1], d[i-1][2]) + rgb[i][0]
    d[i][1] = min(d[i-1][0], d[i-1][2]) + rgb[i][1]
    d[i][2] = min(d[i-1][0], d[i-1][1]) + rgb[i][2]

print(min(d[n-1]))