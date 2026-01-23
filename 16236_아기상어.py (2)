import sys
input=sys.stdin.readline
from collections import deque


# li[y1][x1] = 아기상어 좌표 , li[y2][x2] = 거리 구하고싶은 물고기의 좌표
def find_eatfish(li,y1,x1):
    global size # 아기 상어의 현재 크기
    global eatfish # 배열
    visited=[[False for _ in range(n)] for _ in range(n)]
    # 좌,우,위,아래
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    # -------------
    q=deque()
    q.append([y1,x1,0]) # 초기좌표
    visited[y1][x1]=True
    zdist=-1
    
    while q:
        ar=q.popleft()
        y=ar[0] # 지역변수 y,x 로, 바깥에 있는 아기상어 좌표 y,x랑 별개임
        x=ar[1]
        dist=ar[2]
        if (zdist!=-1):
            if (dist>zdist): # 배열안엔 거리=zdist인 좌표만
                return zdist

        if (li[y][x]<size and li[y][x]!=0): # 물고기 찾았을때
            zdist=dist
            eatfish.append([y,x,dist])

        for i in range(0,4):
            ny=y+dy[i]
            nx=x+dx[i]
            if (nx<0 or ny<0 or nx>n-1 or ny>n-1):
                continue
            if (li[ny][nx]<=size and visited[ny][nx]==False):
                q.append([ny,nx,dist+1])
                visited[ny][nx]=True

    # 물고기 찾았지만 , dist가 최대 거리일때
    if (zdist!=-1): 
        return zdist
    # 모든 통로가 막혔을때
    return 1557

n=int(input().strip())
li=[]
for _ in range(n):
    li.append(list(map(int,input().split())))


# 아기 상어 위치 구하기
y=-1
x=-1
for i in range(n):
    for j in range(n):
        if (li[i][j]==9):
            y=i
            x=j
            break

# 좌표만 저장하고 초기 아기상어의 위치도 빈칸(0)으로 변경            
li[y][x]=0
# ------------
size=2
tp=0
# 총 아기 상어가 이동한 거리(answer)
ans=0
while 1:
    eatfish=[] #([y,x,dist])
    dist1=find_eatfish(li,y,x)
    if (dist1==1557):
        break
    eatfish.sort(key=lambda x:(x[0],x[1]))
    ans+=dist1 
    y=eatfish[0][0] # 위치 이동
    x=eatfish[0][1]
    li[y][x]=0
    tp+=1
    if (tp==size):
        size+=1
        tp=0

print(ans)
