n=int(input())
def ctime(time1):
    a=time1//100
    r=time1%100
    return a*60 + r - 600 


time_arr=[]
arr=[0] * 721
for _ in range(n):
    start,end=map(int,input().split())
    time_arr.append([start,end])


for se in time_arr:
    s=ctime(se[0])
    e=ctime(se[1])
    for a in range(s-10,e+10):
        if a<0 or a>720:
            continue
        arr[a]=1 # 1 = 쉬지 못하는 시간

anstime=0
cnt=0
for t in arr:
    if t==1:
        anstime=max(anstime,cnt)
        cnt=0
    elif t==0:
        cnt+=1

anstime=max(anstime,cnt-1) # 끝나고 한번더 해줘야함 (근데 마지막이 껴있는거는 22:00 에도 cnt가 증가한게 반영되므로 cnt-1로 해줘야함)
print(anstime)