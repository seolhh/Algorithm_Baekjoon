lst=[int(input()) for _ in range(8)]
dic = { lst[i]:i for i in range(len(lst))}
# print(dic)
a=sorted(dic.items(), key= lambda x: x[0], reverse=True)
cnt = 0
index_lst=[]
for i in range(len(a[:5])):
    cnt+=a[i][0]
    index_lst.append(a[i][1])
index_lst.sort()
print(index_lst)
print(cnt)
print(*list(map(lambda x: x+1 ,index_lst)))
