# [백준 : 1912번] 연속합
n = int(input()) # 임의의 수열 개수
array = list(map(int, input().split()))

d = [-1000]*(n+1)

d[0] = array[0]

for i in range(1, n):
    d[i] = max(array[i], d[i-1]+array[i])

print(max(d))