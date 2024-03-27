# [백준 : 16401번] 과자 나눠주기
# 이진 탐색
# M : 조카의 수, N : 과자의 수
m, n = map(int, input().split())
# 과자 길이
snack = list(map(int, input().split()))

start = 1 # 과자 최소 길이
end = max(snack) # 주어진 과자 길이 중 최대값

result = 0
while(start <= end):
    total = 0
    mid = (start+end) // 2
    # 모든 조카에게 같은 길이의 막대과자를 나눠줄 수 없다면, 0 츌력
    if mid == 0:
        break

    for x in snack:
        if x >= mid:
            total += (x // mid)
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
