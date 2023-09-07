N = int(input())


arr = [[0]*100 for _ in range(100)]
for n in range(N):
    r,c,w,h = map(int,input().split())

    for i in range(r,r+w):
        for j in range(c,c+h):
            arr[i][j]+=1
for cnt in arr:
    print(cnt.count(1))
    print(cnt.count(2))
    print('=========')

#
# for z in arr:
#     print(z)
