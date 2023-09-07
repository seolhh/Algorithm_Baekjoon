# lst = []
#
# for _ in range(9):
#     Num  = int(input())
#     lst.append(Num)
# Sum = sum(lst)
#
# for i in range(len(lst)-1):
#     print(lst[i])
#     for j in range(i+1,len(lst)):
#         print(sum(lst))
#     #     if Sum-(lst[i]+lst[j])==100:
#     #         lst.remove(lst[i])
#     #         print(lst)
#             # lst.remove(lst[j])
#             # lst.sort()
#             # print(lst)
#             # break
# #
# lst = []
# #
# for _ in range(9):
#     Num  = int(input())
#     lst.append(Num)
# Sum = sum(lst)
# print(Sum)
#
# for i in range(len(lst)-1):
#     for j in range(i+1,len(lst)):
#         if Sum-lst[i]-lst[j]==100:
#             print(lst[i])
#             print(lst[j])
#             print(lst)
#             lst.remove(lst[i])
#             print(lst)
#             lst.remove(lst[j])
#             print(lst)
#             lst.sort()
#             print(lst)
#             print(sum(lst))
#             break
lst = []

for _ in range(9):
    Num  = int(input())
    lst.append(Num)
Sum = sum(lst)
# print(Sum)

for i in range(len(lst)-1):
    for j in range(i+1,len(lst)):
        # print(Sum - lst[i] - lst[j])
        if Sum-lst[i]-lst[j]==100:
            lst.remove(lst[j])
            lst.remove(lst[i])
            lst.sort()
            break
for k in lst:
    print(k)
