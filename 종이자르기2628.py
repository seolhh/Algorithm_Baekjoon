R,C = map(int,input().split())  # 가로 세로 길이
N = int(input()) # 자르는 횟수
arr = [list(map(int,input().split()))for _ in range(N)]


r_l=[] # 행
c_l=[] # 열


for i in range(N):
    for j in range(0,2):
        if arr[i][j]==0:  # 가로가 주어질 경우
            r_l.append(arr[i][1])
            r_l.sort()
        elif arr[i][j]==1: # 세로가 주어질 경우
            c_l.append(arr[i][1])
            c_l.sort()


R_lst = [R] # 가로를 열로 자른 리스트
C_lst = [C] # 세로를 행으로 자른 리스트

while True:
    if len(c_l)==0: # 리스트가 비어있을 경우= 다 잘랐을 경우
        break
    else:
        a = R_lst.pop() # 주어진 가로길이
        b=c_l.pop() # 자를 수 있는 열의 경우
        R_lst.append(a-b) # 가로-열
        R_lst.append(b) #다시 남은 길이도 리스트에 담기

while True:
    if len(r_l)==0:
        break
    else:
        a = C_lst.pop()
        b = r_l.pop()
        C_lst.append(a-b)
        C_lst.append(b)

print(max(R_lst)*max(C_lst))

