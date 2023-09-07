N = int(input())
c_lst=[]
r_lst=[]
for i in range(N):
    n,m = map(int,input().split())
    c_lst.append(n)
    r_lst.append(m)
c_lst.sort()
r_lst.sort()

Sum=0
Sum+=(c_lst[-1]+10-c_lst[0])*2
Sum+=(r_lst[-1]+10-r_lst[0])*2
# for i in range(len(c_lst)-1):
#     if c_lst[i]+10<c_lst[i+1]+10:
#         Sum+=((c_lst[i+1]+10)-(c_lst[i]+10))*2
# for j in range(len(r_lst)-1):
#     if r_lst[i]+10<r_lst[i+1]+10:
#         Sum += ((r_lst[i + 1] + 10) - (r_lst[i] + 10)) * 2

