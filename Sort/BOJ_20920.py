# [백준 : 20920번] 영단어 암기는 괴로워
# 정렬 알고리즘
from collections import defaultdict
# n : 영어 지문에 나오는 단어의 개수, m : 외울 단어의 길이
n, m = map(int, input().split())

word = []
for _ in range(n):
    arr = input()
    # m 이상인 단어
    if len(arr) >= m:
        word.append(arr)

# 단어가 나오는 횟수
result = defaultdict(int)
for i in word:
    result[i] += 1

# 1. 자주 나오는 단어, 2. 단어의 길이, 3. 사전 순서로 정렬
sorted_result = sorted(result, key = lambda x: (-result[x], -len(x), x))

for i in range(len(sorted_result)):
    print(sorted_result[i])