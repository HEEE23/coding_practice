# [백준 : 2579번] 계단 오르기
# DP
n = int(input()) # 계단의 개수

score = [0]*301 # 각 계단에 쓰여 있는 정수
for i in range(1,n+1):
    score[i] = int(input())

d = [0] * 301

d[1] = score[1]
d[2] = score[1] + score[2]
d[3] = max(score[1]+score[3], score[2]+score[3])

for i in range(4,n+1):
    # i-1번째 계단으로 올라온 경우, i-2번째 계단에서 올라온 경우
    d[i] = max(d[i-3] + score[i-1] + score[i], d[i-2] + score[i])

print(d[n])