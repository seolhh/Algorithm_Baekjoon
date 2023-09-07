H, W = map(int,input().split())
arr =[list(input()) for _ in range(H)]

# for k in arr:
#     # print(k)


for r in range(H):
    for c in range(W):
        if arr[r][c]=='.':
            arr[r][c]=-1
        else:
            arr[r][c]=0

