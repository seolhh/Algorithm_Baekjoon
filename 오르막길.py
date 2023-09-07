N = int(input())
lst = list(map(int,input().split()))

Max = 0
m=0

for i in range(N-1):
    if lst[i]>=lst[i+1]:
        m=0
        continue
    if lst[i]<lst[i+1]:
        m+=(lst[i+1]-lst[i])
        Max=max(Max,m)
print(Max)
    #     if
    # Max=max(Max,m)
    #     print(Max)