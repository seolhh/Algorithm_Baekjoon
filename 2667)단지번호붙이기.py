# 구해야 하는 것 : 단지의 수, 각 단지에 속한 집의 수 리스트
# 2차원배열 돌면서 1 = 집이 있는것
# cnt ==0 인데, 단지 하나당 있는 집의 개수를 뜻함. 따라서 단지가 바뀌면 reset 해줘야한다,

# 1을 만나면 Q에 넣어줌 -> 값을 0으로 바꿈 (그래야 다음에 거기 안걸림), cnt+=1올려준다.
# Q에서 popleft를 한다. -> 그 값에 대한 로직 시작(DFS) 각 Q로직을 실행 할 때,total 올려줌

# DFS로직
# for문으로 popleft한 값이 있는 배열의 위치부터 델타로 상하좌우 돈다.
# 돌면서 또 1을 만나면 그 값을 cnt+=1,0으로 바꿔주고, Q에 넣어준다.

from collections import deque

N = int(input())   # 배열의 크기
arr = [list(map(int, input())) for _ in range(N)]   # 2차원배열 input 방법
# print(arr)

total = []

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for i in range(N):
    for j in range(N):
        if arr[i][j] ==1:
            Q =deque()
            Q.append((i,j))
            cnt = 1
            arr[i][j] = 0

            while Q:
                r,c = Q.popleft()

                for idx in range(4):
                    nr = r + dr[idx]
                    nc = c + dc[idx]

                    if 0<=nr<N and 0<=nc<N and arr[nr][nc]==1:
                        cnt+=1
                        arr[nr][nc] = 0
                        Q.append((nr,nc))
            total.append(cnt)

print(len(total))

for i in sorted(total):
    print(i)





