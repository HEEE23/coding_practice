# [백준 : 14501번] 퇴사
# DP
n = int(input()) # 퇴사하기 전 남은 일수

t = [] # 상담을 완료하는데 걸리는 기간
p = [] # 상담을 했을 대 받을 수 있는 금액
d = [0 for _ in range(n+1)]

for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

for i in range(n-1,-1,-1): # 역순
    if t[i] + i > n: # 상담 기간이 퇴사일을 넘긴 경우
        d[i] = d[i+1]
    else: # 상담 기간이 퇴사일을 넘기지 않은 경우
        d[i] = max(d[i+1], d[t[i]+i] + p[i]) # i일에 상담을 안 할 경우, 상담을 할 경우 중 최대 수익

print(d[0])