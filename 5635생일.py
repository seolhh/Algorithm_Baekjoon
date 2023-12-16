n = int(input())
st=[]
for i in range(n):
    n, d, m, y = input().split()
    st.append([n, int(d), int(m), int(y)])  # 2차원으로 리스트 추가
st.sort(key=lambda x: (x[3], x[2], x[1]))  # 년,월,일 순으로 정렬
print(st[-1][0])  # 가장 나이 적은 사람
print(st[0][0])
    # lst.append(list( input().split()))
    # print(lst)

# 각 리스트의 3번째 비교, 2번째, 1번째 내려와야 함.
# lst는 가장 큰 list 그 안에 for문으로 n개 돌고 그 안에서 또 찾기.

