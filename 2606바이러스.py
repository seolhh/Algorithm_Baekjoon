N = int(input()) # 컴퓨터 개수
M = int(input())  # 연결선 개수
G = [[] for i in range(N+1)]   #이부분이 graph = [[] for i in range(computer+1)] 빈 개수만큼 있는 2차원배열 생성

def dfs(c):
    global cnt

    cnt+=1
    visited[c] = 1
    for n in G[c]:
        if not visited[n]:
            dfs(n)



for i in range(M):   # 그래프에 수 넣는거
    index,num = map(int,input().split())
    G[index].append(num)
    G[num].append(index)  # ????? 이건 왜 해줘야 하지? -> 방향이 정해져 있지 않으니까 양방향 가능
# print(G)
cnt =0
visited = [0]*(N+1)  # ????? 연결선 개수만큼만 있으면 안되나? -> 0번은 안쓰니까 N+1개 필요
dfs(1)
print(cnt-1)



