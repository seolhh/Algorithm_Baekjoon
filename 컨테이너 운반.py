'''
for문 사용
T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    n_lst = list(map(int,input().split())) #컨테이너 나열
    m_lst = list(map(int, input().split())) #트럭 나열
    n_lst.sort(), m_lst.sort()
    n_lst.reverse() # 컨테이너 큰 것부터 정렬
    m_lst.reverse() #트럭 큰 것부터 정렬
    print(n_lst , m_lst)


# for문 사용
    cnt = 0
    for b in n_lst: # 컨테이너 반복
        for t in m_lst: # 트럭 반복
            if b<=t:
                cnt+=b
                m_lst.pop(0)# 트럭에 적재 가능하면 사용한 트럭은 없애줘야 함 
                break # break하면 n_lst for문으로 다시 반복 
    print(cnt)
'''

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    n_lst = list(map(int,input().split())) #컨테이너 나열
    m_lst = list(map(int, input().split())) #트럭 나열
    n_lst.sort(), m_lst.sort()


    result=0
    while True:
        if len(n_lst)==0 or len(m_lst)==0:
            break

        if n_lst[-1] <= m_lst[-1]:
            result += n_lst.pop()
            m_lst.pop()
        else:
            n_lst.pop()
    print(f'#{tc} {result}')