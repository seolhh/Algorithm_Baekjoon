lst =[]
for _ in range(10):
    n = int(input())
    lst.append(n)

for i in range(10):
    before = lst[i]
    after = lst[i+i+1]
    print(before, after)