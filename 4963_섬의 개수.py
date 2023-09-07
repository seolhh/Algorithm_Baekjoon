from collections import deque


total = []

def BFS(r,c):

    Q = deque()
    Q.append((r,c))
    arr[r][c]=0
         #상  하  좌  우 좌상 좌하 우상 우하
    dr = [-1, 1, 0, 0, -1, 1, -1, 1]
    dc = [0, 0, -1, 1, -1, -1, 1, 1]

    while Q:
        r,c = Q.popleft()  # 다음 옆에 있는 1을 찾으려면 Q에서 꺼내줘야 한다.

        for idx in range(8):
            nr = r + dr[idx]
            nc = c + dc[idx]
            if 0<=nr<h and 0<=nc<w and arr[nr][nc]==1:
                Q.append((nr,nc))
                arr[nr][nc]=0






while True:
    w,h =map(int,input().split())
    if w == 0 and h == 0:    # 0을 만나면 배열도 안만들고 끝내야 함
        break

    arr = [list(map(int,input().split()))  for _ in range(h)]

    cnt = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j]==1:
                BFS(i,j)
                cnt += 1

    total.append(cnt)


for i in total:
    print(i)


