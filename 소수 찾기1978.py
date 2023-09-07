N = input()
n_lst = map(int,input().split())

cnt=0

for i in n_lst:
    error=0
    if i>1:
        for j in range(2,i-1):
            if i % j==0:
                error +=1
        if error==0:
            cnt+=1

print(cnt)

