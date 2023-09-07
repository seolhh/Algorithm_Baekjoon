t=int(input())
for tc in range(t):
    n=int(input())
    Max = []
    Max_name = []
    for p in range(n):
        C, name =input().split()
        Cost=int(C)
        Max.append(Cost)
        Max_name.append(name)
    idx=Max.index(max(Max))
    print(Max_name[idx])