N = int(input())
arr = [list(map(int,input().split())) for i in range(N)]
# print(arr)

dp = [[0]*N for i in range(N)]

dp[0][0] = arr[0][0]  # 가장 첫번째 값은 그보다 앞의 수가 없어서 그냥 넣어놓고 시작

for i in range(1, N):
    for j in range(0,i+1):   # i가 1일때 리스트 안에 값은 i+1개 있으니까
        if j ==0: # 가장 좌측은 무조건 자기 앞줄의 값이랑만 더할 수 있으니까
            dp[i][j] = dp[i-1][j] + arr[i][j] # 지금까지 더해진 값(dp에 누적합) + 새로 더할값(arr에 있음)
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])+arr[i][j]

print(max(dp[N-1]))




