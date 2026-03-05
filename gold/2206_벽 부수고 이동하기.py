from collections import deque
dn=[-1,1,0,0]
dm=[0,0,-1,1]
def bfs1(li,n,m):
    visited=[[False for _ in range(m)] for _ in range(n)]
    visited2=[[False for _ in range(m)] for _ in range(n)]
    q=deque()
    q.append([0,0,1,0]) # 세로(n)좌표 , 가로(m)좌표 , 거리 , 벽 부순 횟수
    visited[0][0]=True
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
            
            # 1번 뚫고온 케이스랑 0번 뚫고온 케이스의 경로가 겹칠 수 있음.
            # 실제 답은 0번 뚫고온 케이스의 경로를 지나가는데 1번 뚫고온 케이스가 visited를 침범해 버리면 0번 케이스의 경로가 씹힘.
            # 따라서 0번 뚫고온 케이스랑 1번 뚫고온 케이스 따로따로 visited 배열을 만들어서 처리하는 풀이를 고안했음
            if (break1==0):
                if (visited[ny][nx]==False):
                    # break1 = 0 or 1
                    # break1=2 가 되는 블록은 아예 visited도 못하게 queue에 추가부터 하지 않는다.
                    
                    visited[ny][nx]=True
                    q.append([ny,nx,dist+1,break1+1])
                    
                        
            elif (break1==1):
                if (visited2[ny][nx]==False):
                    # break1 = 0 or 1
                    # break1=2 가 되는 블록은 아예 visited도 못하게 queue에 추가부터 하지 않는다.
                    if (li[ny][nx]=='1'):
                         continue
                    elif (li[ny][nx]=='0'):
                        visited2[ny][nx]=True
                        q.append([ny,nx,dist+1,break1])

    return -1

n,m=map(int,input().split())
li=[]
for _ in range(n):
    arr=list(input()) # 길이 m
    li.append(arr)
    

ans=bfs1(li,n,m)
print(ans)
