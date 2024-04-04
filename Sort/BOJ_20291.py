# [백준 : 20291번] 파일 정리
# n : 파일의 개수
from collections import defaultdict
n = int(input())

# 확장자 저장
ext = []
for i in range(n):
    file_name = list(input().split('.'))
    ext.append(file_name[1])

# key : 확장자 파일의 이름, value : 확장자 파일의 개수
num = defaultdict(int)
for i in ext:
    num[i] += 1

# (key, value) 쌍을 x에 넣어 key 값을 기준으로 사전 순으로 정렬
sorted_num = sorted(num.items(), key = lambda x:x[0])

for i in range(len(sorted_num)):
    print(' '.join(map(str,sorted_num[i])))