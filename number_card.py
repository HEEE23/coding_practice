# [백준 : 10815번] 숫자 카드
# 이진 탐색
def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

# 상근이가 가지고 있는 숫자 카드의 개수
n = int(input())
# 숫자 카드에 적혀있는 정수
num = list(map(int, input().split()))
# 비교할 카드 개수
m = int(input())
# 상근이가 가지고 있는 숫자 카드인지 아닌지를 구해야 할 정수
card = list(map(int, input().split()))

num.sort()

# 각 수가 적힌 숫자 카드를 상근이가 가지고 있으면 1, 아니면 0
for i in range(m):
    if binary_search(num, card[i], 0, n - 1) == None:
        print("0", end = ' ')
    else:
        print("1", end = ' ')
