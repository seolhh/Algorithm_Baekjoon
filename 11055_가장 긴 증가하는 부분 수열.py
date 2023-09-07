N = int(input())
num_lst = [0] + list(map(int,input().split()))   # 왜 앞에 0을 더해줘야 하는지?- 인덱스를 맞춰야 하는데 0부터 있으면 안맞으니까

dp = [0]*(N+1)

#dp[i]에 대한 정의 = i번째 인덱스에 있는 수가 뭔지 모르지만 거기까지 구하면 가장 긴 길이가 나온다

for i in range(1, N+1): # 1부터 나 전체 도는 법
    mx = 0
    for j in range(0,i): # 처음부터 나 직전까지 돌면서 max 찾기
        if num_lst[i]>num_lst[j]:
            mx = max(mx,dp[j])   # 내 앞에까지 수 중에서 가장 큰 값
    dp[i] = mx +1
    # 무조건 마지막이 큰게 아니라 중간에 가장 큰 연속값이 나오고 그 뒤에 다시 초기화 될 수도 있어서 꼭 max 구하기
print(max(dp))   # dp들 중에서 가장 큰 값까지가 연속으로 증가하는 부분 수열이니까.


