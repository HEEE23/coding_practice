# [백준 : 18870번] 좌표 압축
n = int(input()) # 좌표의 수
X = list(map(int, input().split()))

# X의 값을 중복 제거한 후 리스트로 만들고 정렬
X_sort = sorted(list(set(X)))

# X_sort를 이용해 딕셔너리 구성
dic = {}
for i in range(len(X_sort)):
    dic[X_sort[i]] = i

for i in X:
    print(dic[i], end = ' ')