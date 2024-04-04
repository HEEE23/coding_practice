# [백준 : 18869번] 멀티버스 II
from collections import defaultdict
# m : 우주의 개수, n : 행성의 개수
m, n = map(int, input().split())

universe = defaultdict(int)

for i in range(m):
    #  각 우주에 있는 행성의 크기
    planet = list(map(int, input().split()))

    # 행성 크기 오름차순 정렬
    sortedplanet = sorted(list(set(planet)))

    # 정렬된 행성에 대한 순위를 딕셔너리로 저장
    rank = {sortedplanet[i] : i for i in range(len(sortedplanet))}

    # 입력 받은 행성 크기를 딕셔너리로 저장한 순위를 사용하여 튜플로 저장
    vector = tuple([rank[i] for i in planet])

    # key : 순위 벡터, value : 해당 순위 벡터가 등장한 횟수
    universe[vector] += 1

sum = 0
# 우주의 쌍 구하기 nC2
for i in universe.values():
    sum += (i * (i - 1)) // 2

print(sum)