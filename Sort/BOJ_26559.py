# [백준 : 26559번] Friends
n = int(input())

for _ in range(n):
    m = int(input())

    # 이름, 숫자 입력
    names_nums = [input().split() for _ in range(m)]

    # 숫자에 따라 이름 정렬(내림차순)
    names_nums.sort(key=lambda x: int(x[1]), reverse=True)

    result = []
    for names in names_nums:
        result.append(names[0])

    print(', '.join(result))