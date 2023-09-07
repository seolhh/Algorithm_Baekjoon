stu = int(input())
lst = list(map(int,input().split()))
line_lst =[ ]
for i in lst:
    if i not in line_lst:
        line_lst.append(i)
print(line_lst)
    else:
        line_lst.insert(i,i+1)
for j in line_lst:
    all_lst = line_lst[j]+1