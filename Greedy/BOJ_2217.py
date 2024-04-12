# [백준 : 2217번] 로프
n = int(input()) # n : 로프의 개수
weight = [int(input()) for _ in range(n)] # 각 로프가 버틸 수 있는 최대 중량
weight.sort() # 중량 오름차순 정렬
count = len(weight) # 사용할 로프의 개수

result = []
for i in range(n):
    result.append(count * weight[i])
    count -= 1

print(max(result))