# def dfs(n,sm):  # n은 선수 , sm은 모든 포지션 능력치 최대 합
#     global Max
#     if n==11:
#         Max= max(sm,Max)
#         return
#
#     for j in range(11): # 포지션
#         if V[j]==1:
#             continue
#         if arr[n][j]==0:
#             continue
#         V[j]=1
#         dfs(n+1, sm+arr[n][j])
#         V[j]=0
#
# T = int(input())
# for tc in range(T):
#     arr = [list(map(int,input().split())) for _ in range(11)]
#     V = [0]*11   # 포지션
#     Max = 0 # 능력치의 합 최대값 변수
#
#     dfs(0,0)
#     print(Max)



def dfs(n,sm):
    global Max
    if n==11:  # n= 선수의 수 (깊이)가 11이 되면 종료
        Max=max(sm,Max)
        return


    for i in range(11): # 깊이를 11번 돌면서(n을 올려주기 위해)
        if V[i]==1:     # 만약 이미 방문해서 1이 올라가 있으면 continue
            continue
        if arr[n][i]==0: # 포지션 능력이 0이면 continue
            continue
        V[i]=1           # 위의 조건 다 통과하면 V 1로 바꿔줌
        dfs(n+1, sm+arr[n][i])
        V[i]=0            # 초기화 해줘야 i 바뀔때 마다 다시 시작 가능


T = int(input())
for tc in range(T):
    arr =[list(map(int,input().split())) for _ in range(11)]
    V = [0]*11  # 포지션 방문 여부 확인 할 리스트
    Max = 0     # 최대값을 찾기위한 조건
    dfs(0,0)    #깊이 0에서 시작, 합계 0에서 시작
    print(Max)

