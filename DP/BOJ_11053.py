# [백준 : 11053번] 가장 긴 증가하는 부분 수열
# DP
n = int(input()) # 수열 A의 크기
a = list(map(int, input().split())) # 수열 A

d = [0]*(n+1)

d[0] = 1

for i in range(1, n):
    for j in range(i):
        if a[i] > a[j]:
            d[i] = max(d[i], d[j]+1)
        else:
            d[i] = max(d[i], 1)

print(max(d))