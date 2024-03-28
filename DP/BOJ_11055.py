# [백준 : 11055번] 가장 큰 증가하는 부분 수열
# DP
n = int(input()) # 수열 A의 크기
A = list(map(int, input().split())) # 수열 A

d = [0] * n
d[0] = A[0]

for i in range(1, n):
    for j in range(i):
        # 증가하는 부분 수열이 만들어진 경우
        if A[i] > A[j]:
            d[i] = max(d[i], A[i]+d[j])
        # 증가하는 부분 수열이 만들어지지 않은 경우
        else:
            d[i] = max(d[i], A[i]) # d값, 현재 A의 값 중 큰 값

print(max(d)) # A의 합이 가장 큰 증가하는 부분 수열의 합