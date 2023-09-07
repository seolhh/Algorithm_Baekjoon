N,M= map(int,input().split())
lst=[]
for i in range(1,M+1):
    for _ in range(i):
        if len(lst)==M: break
        else: lst.append(i)
lst=[0]+lst
print(lst)

