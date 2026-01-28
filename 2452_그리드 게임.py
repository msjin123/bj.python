from collections import deque
# ------------------------------------------------------------
def make_li2(m,n,li,li2):
    global visited
    
    # li2 만들기
    groupnum=0
    for i in range(0,m):
        for j in range(0,n):
            if visited[i][j]==False:
                groupnum+=1
                if li[i][j]==0:
                    bfs(m,n,li,i,j,0,groupnum)
                    
                elif li[i][j]==1:
                    bfs(m,n,li,i,j,1,groupnum)

    return groupnum # 그룹의 갯수
    
def bfs(m,n,li,i,j,num,groupnum): # num = 0 or 1  groupnum = 그룹 1 그룹 2 ...
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]

    q=deque()
    q.append([i,j])
    li2[i][j]=groupnum
    visited[i][j]=True
    while q:
        a=q.popleft()
        y=a[0]
        x=a[1]
        for c in range(0,4):
            ny=y+dy[c]
            nx=x+dx[c]
            if (nx<0 or ny<0 or nx>n-1 or ny>m-1):
                continue
            if (visited[ny][nx]==False and li[ny][nx]==num):
                visited[ny][nx]=True
                q.append([ny,nx])
                li2[ny][nx]=groupnum

# ------------------------------------------------------------
def make_comp(m,n):
    global comp
    
    dx=[1,0]
    dy=[0,1]
    for y in range(0,m):
        for x in range(0,n):
            g1=li2[y][x]
            for k in range(0,2):
                ny=y+dy[k]
                nx=x+dx[k]
                if (nx<0 or ny<0 or nx>n-1 or ny>m-1):
                    continue
                g2=li2[ny][nx]
                if (g1!=g2):
                    comp[g1].add(g2)
                    comp[g2].add(g1)
                
              
# ------------------------------------------------------------  
def finding_bfs3(group,ans):
    global stamp,vis,dist
    
    stamp+=1
    q=deque()
    q.append(group)
    vis[group]=stamp # 방문체크
    dist[group]=0
    far_node=group
    far_dist=0
    while q:
        a=q.popleft()
        g=dist[a]

        if (g>=ans):
            return None,10001
        if (g>=far_dist):
            far_dist=g
            far_node=a
            

        for ng in comp[a]:
            if (vis[ng]!=stamp):
                vis[ng]=stamp
                dist[ng]=g+1
                q.append(ng)

    return far_node,far_dist

# -------------------------------------------------- 
def bfs_dist(start):
    global stamp,dist,vis
    q=deque()
    q.append(start)
    stamp+=1
    dist[start]=0
    vis[start]=stamp
    res=[-1]*(groups+1)
    res[start]=0
    while q:
        v=q.popleft()
        g=dist[v]
        for nm in comp[v]:
            if (vis[nm]!=stamp):
                vis[nm]=stamp
                dist[nm]=g+1
                res[nm]=g+1
                q.append(nm)
    return res

# --------------------------------------------------           
ans=10001         

m,n=map(int,input().split()) # 바깥,안
li=[]
for _ in range(m):
    arr=list(map(int,input().split()))
    li.append(arr)

visited=[[False for _ in range(n)] for _ in range(m)] # li2 만들기용
li2=[[0 for _ in range(n)] for _ in range(m)] # group (global)
groups=make_li2(m,n,li,li2) # groups = 그룹의 개수

comp=[set() for _ in range(0,groups+1)]
make_comp(m,n) # 인접 리스트

comp=[list(s) for s in comp]
 
# -------------------------------------
stamp=0
vis=[0 for _ in range(groups+1)]
dist=[0 for _ in range(groups+1)]
# -------------------------------------
a,_=finding_bfs3(1,10001)
b,diam=finding_bfs3(a,10001) # a에서 가장 먼 노드 번호 = b , 거리=diam
lower=(diam+1)//2
# -------------------------------------


distA=bfs_dist(a)
distB=bfs_dist(b)

order=list(range(1,groups+1))    
order.sort(key=lambda x: max(distA[x],distB[x]))
# ans=max(distA[order[0]],distB[order[0]])

for group in order: # ans 값이 작게 나올 수 있는 순서대로 탐색
    _,e=finding_bfs3(group,ans)
    if (e<ans): # 1차 컷팅
        ans=e
        if (ans==lower): # 2차 컷팅 (하한에 도달하면 바로 종료)
            break


print(ans)
