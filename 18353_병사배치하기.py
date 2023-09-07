# 병사를 배치하는 방법은 내림차순
# 내림차순은 중간에 순서가 안맞는 수를 열외하는 방식으로 진행
# 열외해야 하는 병사 수를 구하면 되니까 병사 한명을 뺄 때마다 cnt +=1
# 병사를 빼는 방법은 점화식에서 앞에 수보다 뒤에 오는 수가 크면 걔는 제외시키기

N = int(input())
num_lst =[0] + list(map(int,input().split()))
dp = [0] *(N+1)

cnt=0

for i in range(1,N+1):
    for j in range(0,i):
        print(num_lst[i], num_lst[j])


