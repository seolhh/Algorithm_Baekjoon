
arr = [[0]*100 for _ in range(100)]
for n in range(4):
    lx, ly, rx, ry = map(int, input().split())

    for r in range(lx,rx):
        for c in range(ly,ry):
            arr[r][c]=1

# cnt = 0
# for i in range(100):
#     for j in range(100):
#         if arr[i][j]==1:
#             cnt+=1
# print(cnt)

Sum = 0
for i in arr:
    Sum += sum(i)

print(Sum)


