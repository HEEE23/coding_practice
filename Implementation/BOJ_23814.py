# [백준 : 23814번] 아 저는 볶음밥이요
# D : 군만두 서비스를 제공하는 주문 수
D = int(input())
## N : 짜장면 시킨 사람의 수, M : 짬뽕을 시킨 사람의 수, K : 남은 사람의 수
N, M, K = map(int,input().split())

# mandoo : 군만두 서비스 개수, 볶음밥 주문 수, mixed_rice : 주문한 볶음밥의 수
total_mandoo = []
mixed_rice = []

A = D - N%D # 군만두 서비스를 받기 위해 필요한 짜장면 주문 수
B = D - M%D # 군만두 서비스를 받기 위해 필요한 짬뽕 주문 수

## 메뉴에 따른 군만두 개수 경우의 수
# 경우 1. 모두 볶음밥으로 주문한 경우
total_mandoo.append(N//D + M//D + K//D)
mixed_rice.append(K)

# 경우 2. 볶음밥에서 짜장면으로 주문한 경우
total_mandoo.append((N+A)//D + M//D + (K-A)//D)
mixed_rice.append(K-A)

# 경우 3. 볶음밥에서 짬뽕으로 주문한 경우
total_mandoo.append(N//D + (M+B)//D + (K-B)//D)
mixed_rice.append(K-B)

# 경우 4. 볶음밥에서 짜장면, 짬뽕 모두 주문한 경우
total_mandoo.append((N+A)//D + (M+B)//D + (K-A-B)//D)
mixed_rice.append(K-A-B)

ZIP = list(zip(total_mandoo, mixed_rice))
ZIP.sort(key = lambda x:(-x[0],-x[1])) # 내림차순 정렬
print(ZIP[0][1]) # 군만두를 가장 많이 받을 수 있으면서 주문할 수 있는 볶음밥의 최대 개수
