# [백준 : 10825번] 국영수
# n : 도혁이네 반의 학생의 수
n = int(input())

dic = {}
for i in range(n):
    name, kor, eng, math = input().split()
    dic[name] = [int(kor), int(eng), int(math)]

# 우선순위 : 1. 국어 점수 감소, 2. 영어 점수 증가, 3. 수학 점수 감소, 4. 사전 순
sorted_name = sorted(dic, key = lambda x: (-dic[x][0], dic[x][1], -dic[x][2], x))

for i in range(len(sorted_name)):
    print(sorted_name[i])