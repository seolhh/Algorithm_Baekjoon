# 범위를 벗어나거나 이미 숫자가 있으면 회전
# 범위를 벗어나지 않게 조건 넣기
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    # print(arr)
        # 우, 하, 좌, 상
        # 0,  1, 2, 3
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    r=0
    c=0
    arr[r][c]=1
    idx = 0
    for i in range(2,N*N+1):
        nr = r+dr[idx]
        nc = c+dc[idx]
        if 0<=nr<N and 0<=nc<N and arr[nr][nc]==0:
            r=nr
            c=nc
            arr[r][c]=i
        else:
            idx=(idx+1)%4
            r = r + dr[idx]
            c = c + dc[idx]
            arr[r][c]=i
    print(f'#{tc}')
    for k in arr:
        print(*k)


        # idx = (idx+1)%4




