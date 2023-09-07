N,K = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
print(arr)

# 리스트에 있는 값을 이용해서 딕셔너리 만들기
# a_dic={}
# 1
# for i in arr:
#     a_dic[i[0]]=i[1:]
# print(a_dic)

# 2
# for i, *j in arr:
#     a_dic[i]=[*j]
# print(a_dic)
#
#
# Max=0
# for i in a_dic.values():
#     if Max<i[0]:

for i in arr:
    for j in range(4):
        print(arr[i][j])