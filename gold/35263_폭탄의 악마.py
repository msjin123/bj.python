import sys
input=sys.stdin.readline

import math as m

n,m=map(int,input().split())
lst=list(map(int,input().split())) # 원래
lst2=[] # 소인수 기댓값 
for a in range(0,n):
    b=lst[a]
    
    # 소인수분해하고, 소인수들 추출 (arr에 추출)
    arr=set()
    divnum=2
    while(divnum<=int(b**0.5)):
        if (b%divnum==0):
            arr.add(divnum)
            b=b//divnum
        else:
            divnum+=1
    if (b>1):
        arr.add(b)

    average=sum(arr)/len(arr)
    lst2.append(average) # lst2[a]=average
# -------------------------------------------
# ck=[False] * (n+1)
# for _ in range(m):
#     i,j=map(int,input().split())
#     for num in range(i,j+1):
#         ck[num]=True

diff=[0] * (n+2)
for _ in range(m):
    i,j=map(int,input().split())
    diff[i]+=1
    diff[j+1]-=1


# ---------------------------------------

# (참고) cover이 음수는 될 수 없다
ans=0
cover=0
for a in range(0,n):
    cover+=diff[a+1]
    if (cover>0):
        ans+=lst2[a]
    else:
        ans+=lst[a]


            
print(ans)
// 
