# N과 M 사이의 값들을 다 돌면서 완전 제곱수를 찾는다
# 완전제곱수 판별법 = n*n
# N과 M이 10000사이의 수니까 100*100까지 가능
# n이 1~100까지를 돌면서 n*n한 값이 내가 가지고있는 값가 같으면 새로운 리스트에 append



N=int(input())
M=int(input())

lst = []
num_lst=[]
for i in range(1,101):
    num = i*i
    if num<N:
        continue
    elif num >= N and num <= M:
        num_lst.append(num)

for i in range(N,M+1):
    if i in num_lst:
        lst.append(i)

lst.sort()


if len(lst)!=0:
    print(sum(lst))
    print(lst[0])
else:
    print(-1)


import math
