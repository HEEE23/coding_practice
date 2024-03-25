# [백준 : 1822번] 차집합
# 이진 탐색
def binary_search(arr, target, start, end):
    while start<=end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None

# 집합 A, B의 원소 개수
a, b = map(int, input().split())
arr_a = list(map(int, input().split())) # 집합 A 원소
arr_b = list(map(int, input().split())) # 집합 B 원소

arr_b.sort()

count = 0
result = []
for i in range(a):
    if binary_search(arr_b, arr_a[i], 0, b-1) == None:
        count += 1
        result.append(arr_a[i])

result.sort() # 오름차순 정렬
# 집합 A에는 속하면서 집합 B에는 속하지 않는 원소가 없다면 0 출력
if len(result) == 0:
    print("0")
else:
    # 집합 A에는 속하면서 집합 B에는 속하지 않는 원소의 개수 출력
    print(count)
    # 구체적인 원소
    for i in range(len(result)):
        print(result[i], end = ' ')
