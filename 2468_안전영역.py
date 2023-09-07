from collections import deque


def BFS(water):
    global ans

    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    visited = [[0]*N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > water and visited[i][j]==0 : # 하나의 칸이 정해진 수면 보다 크고, 아직 간적 없는 주변 탐색 가능
                Q=deque() # 가능 하면 Q에 넣기
                Q.append((i,j))
                visited[i][j]= 1
                cnt +=1


                while Q:
                    r,c =Q.popleft()

                    for idx in range(4):
                        nr = r + dr[idx]
                        nc = c + dc[idx]
                        if 0<= nr < N and 0<= nc < N and visited[nr][nc]==0 and arr[nr][nc] > water:
                            Q.append((nr,nc))
                            visited[nr][nc]=1

    ans = max(ans,cnt)






N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

Max = 0
Min = 101
for i in range(N):
    for j in range(N):
        Max = max(Max,arr[i][j])
        Min = min(Min,arr[i][j])
# print(Max,Min)

ans = 0

for i in range(Min-1, Max):  # 물의 높이 최솟값이 다 똑같을 경우
                             # 안잠기는 경우가 없을 수도 있으니까 최솟값보다 하나라도 작은 케이스에 대한 것도 살펴봐야 함.
    BFS(i)

print(ans)