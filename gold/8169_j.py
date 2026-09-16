n,p=map(int,input().split())

pillars=[]
# grid=[[[0] for _ in range(1001)] for _ in range(1001)]
grid=[]
for _ in range(1001):
    z=[]
    for _ in range(1001):
        z.append(-1)
    grid.append(z)

for _ in range(p):
    x,y=map(int,input().split())
    pillars.append([x,y])

dist=0
one_round=0
for i in range(1,p):
    x1=pillars[i-1][0]
    y1=pillars[i-1][1]
    x2=pillars[i][0]
    y2=pillars[i][1]

    if x1==x2:
        if y1<y2:
            for t in range(y1,y2+1):
                if grid[x1][t]!=-1:
                    continue
                grid[x1][t]=dist
                dist+=1
        elif y1>y2:
            for t in range(y1,y2-1,-1):
                if grid[x1][t]!=-1:
                    continue
                grid[x1][t]=dist
                dist+=1
    elif y1==y2:
        if x1<x2:
            for t in range(x1,x2+1):
                if grid[t][y1]!=-1:
                    continue
                grid[t][y1]=dist
                dist+=1
        elif x1>x2:
            for t in range(x1,x2-1,-1):
                if grid[t][y1]!=-1:
                    continue
                grid[t][y1]=dist
                dist+=1

a=pillars[p-1][0]
b=pillars[p-1][1]
c=pillars[0][0]
d=pillars[0][1]
if a==c:
    if b<d:
        for t in range(b+1,d):
            grid[a][t]=dist
            dist+=1
    elif b>d:
        for t in range(b-1,d,-1):
            grid[a][t]=dist
            dist+=1
elif b==d:
    if a<c:
        for t in range(a+1,c):
            grid[t][b]=dist
            dist+=1
    elif a>c:
        for t in range(a-1,c,-1):
            grid[t][b]=dist
            dist+=1

one_round=dist

# print(pillars)

for _ in range(n):
    x1,y1,x2,y2=map(int,input().split())
    ans=0
    dist1=grid[x1][y1]
    dist2=grid[x2][y2]
    # print(dist1,dist2)
    if dist1<dist2:
        ans=min(dist2-dist1 , dist1+(one_round-dist2))
    elif dist1>dist2:
        ans=min(dist1-dist2 , dist2+(one_round-dist1))
    
    print(ans)
    

# print(grid)