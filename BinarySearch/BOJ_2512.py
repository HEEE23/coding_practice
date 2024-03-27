# [백준 : 2512번] 예산
# 이진 탐색
n = int(input()) # 지방의 수
arr = list(map(int, input().split())) # 각 지방의 예산요청을 표현하는 정수
m = int(input()) # 총 예산을 나타내는 정수

start = 1 # 각 지방의 예산요청을 표현하는 정수의 값은 1 이상
end = max(arr)

result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in arr:
        if x > mid:
            total += x - (x - mid)
        else:
            total += x
    # 예산 한도를 넘지 않는 경우
    if total <= m:
        result = mid
        start = mid + 1
    # 예산 한도 초과
    else:
        end = mid - 1

print(result)
