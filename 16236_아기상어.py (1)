import sys
input=sys.stdin.readline
from collections import deque
n=int(input().strip())
li=[]
for _ in range(n):
    li.append(list(map(int,input().split())))

# li[y1][x1] = 아기상어 좌표 , li[y2][x2] = 거리 구하고싶은 물고기의 좌표
def find_dist(li,y1,x1,y2,x2):
    global size # 아기 상어의 현재 크기
    visited=[[False for _ in range(n)] for _ in range(n)]
    # 좌,우,위,아래
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    # -------------
    q=deque()
    q.append([y1,x1,0])
    visited[y1][x1]=True
    while q:
        ar=q.popleft()
        y=ar[0] # 지역변수 y,x 로, 바깥에 있는 아기상어 좌표 y,x랑 별개임
        x=ar[1]
        dist=ar[2]
        if (y==y2 and x==x2):
            return dist
        for i in range(0,4):
            ny=y+dy[i]
            nx=x+dx[i]
            if (nx<0 or ny<0 or nx>n-1 or ny>n-1):
                continue
            if (li[ny][nx]<=size and visited[ny][nx]==False):
                q.append([ny,nx,dist+1])
                visited[ny][nx]=True
    
    # size보다 작은 물고기지만 , 모든 통로가 막혔을때
    return 1557

def find_answer(li):
    global size
    global y
    global x
    # 총 아기 상어가 이동한 거리(answer)
    ans=0
    # 임시 변수
    atefish=0
    
    while 1:
        caneat_fish=[]
        for i in range(n):
            for j in range(n):
                if (li[i][j]<size and li[i][j]!=0):
                    caneat_fish.append([i,j,find_dist(li,y,x,i,j)]) # [y][x] = 아기 상어의 현재 위치

        # 더이상 먹을 수 있는 물고기가 없는 상태일때
        if (len(caneat_fish)==0):
            break            
        

        
        # 거리순 정렬 , 거리가 같을때는 위부터 , 그다음 왼쪽
        caneat_fish.sort(key=lambda x:(x[2],x[0],x[1]))
        # 매번 정렬된 배열의 첫번째 물고기를 먹는다
        arr=caneat_fish[0]

        # 도달할수없는 물고기의 좌표가 맨 처음에 있다 = 도달할 수 있는 물고기가 없다
        if (arr[2]==1557):
            break
        y=arr[0]
        x=arr[1]
        ans+=arr[2]
        li[y][x]=0 # 먹은 물고기는 빈칸으로
        atefish+=1
        if (atefish==size):
            size+=1
            atefish=0
    return ans


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

# 아기 상어의 크기
size=2


print(find_answer(li))
