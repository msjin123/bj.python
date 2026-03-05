# gemimi 부르기 ctrl+alt+x

from collections import deque
dn=[-1,1,0,0]
dm=[0,0,-1,1]
def bfs1(li,n,m,k):
    visited=[[[False for _ in range(k+1)] for _ in range(m)] for _ in range(n)]
    # ex) k=1 -> 1개 까지 부술수있음 -> visited[][][0],visited[][][1] 2개 필요 -> 길이= k+1
    q=deque()
    q.append([0,0,1,0]) # 세로(n)좌표 , 가로(m)좌표 , 거리 , 벽 부순 횟수
    visited[0][0][0]=True
    while q:
        p=q.popleft()
        y=p[0]
        x=p[1]
        dist=p[2]
        break1=p[3]
        
        if (y==n-1 and x==m-1):
            return dist

        for i in range(0,4):
            ny=y+dn[i]
            nx=x+dm[i]
            
            if (ny<0 or nx<0 or ny>n-1 or nx>m-1):
                continue
            
            if (break1<k and li[ny][nx]=='1' and visited[ny][nx][break1+1]==False):
                
                
                visited[ny][nx][break1+1]=True
                q.append([ny,nx,dist+1,break1+1])
            elif (li[ny][nx]=='0' and visited[ny][nx][break1]==False):
                visited[ny][nx][break1]=True
                q.append([ny,nx,dist+1,break1])
            

    return -1

n,m,k=map(int,input().split()) # 벽을 원래는 1개까지 부술 수 있는데 이걸 k개까지 부술수 있음 k=1~10
li=[]
for _ in range(n):
    arr=list(input()) # 길이 m
    li.append(arr)
    

ans=bfs1(li,n,m,k)
print(ans)
