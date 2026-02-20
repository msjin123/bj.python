# 회의실 배정
import sys
input=sys.stdin.readline
n=int(input().strip())
lst=[]
for _ in range(n):
    start,end=map(int,input().split())
    lst.append([start,end])
lst.sort()


minn=2**31
answer=0
minn=lst[0][1]


for i in range(1,len(lst)):
    if (lst[i][0]>=minn): # '바로 앞' 인덱스까지의 종료시간 최솟값과 현재 시작시간을 비교합니다.
        answer+=1
        minn=2**31

    minn=min(minn,lst[i][1]) # answer+=1 을 한 후, 현재 인덱스부터 다시 시작합니다.
                             # if 문이 만족되지 않을 경우, 만족될떄까지 최솟값만 계속 갱신합니다.
    
print(answer+1)
