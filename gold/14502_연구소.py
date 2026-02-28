import copy
from collections import deque
n,m=map(int,input().split())


li=[]
for _ in range(n):
    li.append(list(input().split()))


answer=0 #남은 0의 개수(안전영역)
# li[0][0] ~ li[n-1][m-1]
# li[a][b]

# num=1부터
def change(num):
    for v in range(1,n+1):
        if (v-1)*m<num<=v*m: #v번쨰 줄일때
            return v-1,(num-(v-1)*m)-1 # num번째에 해당하는 li의 ["첫번쨰"]["두번쨰"] 반환
        
# 왼 오 위 아래 순서
dx=[0,0,-1,1]
dy=[-1,1,0,0]


for i in range(1,n*m-1): #나중에 n,m 이용해서 바꿀꺼임
    for j in range(i+1,n*m): # n*m = 좌표를 숫자로 바꿧을때의 li[n-1][m-1] #j는 li[n-1][m-2] (m>=2 일떄) 까지
        for k in range(j+1,n*m+1):
            
            if i==j or j==k or i==k or i==j==k:
                continue
            
            
            li2=copy.deepcopy(li)
            i0=change(i)[0]
            i1=change(i)[1]
            j0=change(j)[0]
            j1=change(j)[1]
            k0=change(k)[0]
            k1=change(k)[1]
            
            if (li2[i0][i1]=="1" or li2[i0][i1]=="2") or (li2[j0][j1]=="1" or li2[j0][j1]=="2") or (li2[k0][k1]=="1" or li2[k0][k1]=="2"):
                continue
            
            
            else: # 3개의 좌표가 다 "0" 일떄
                li2[i0][i1]="1"
                li2[j0][j1]="1"
                li2[k0][k1]="1"
            # 모든 "2" 에 대해서 bfs 실시
            
            for a in range(0,n):
                for b in range(0,m):
                    if li2[a][b]=="2":
                        queue=deque([(a,b)])
                        while queue:
                            x,y=queue.popleft() # x=세로 y=가로
                            for d in range(0,4): #주변 탐색 (왼 오 위 아래) #하 여기서도 i를 왜써
                                nx=x+dx[d]
                                ny=y+dy[d]
                                if nx<0 or ny<0 or nx>n-1 or ny>m-1:
                                    continue
                                elif li2[nx][ny]=="0": # visited 안한곳만 : visited 완료 된 칸은 "3" 로 바꿀예정 "1" "2" "3" 는 못뚫음
                                    queue.append((nx,ny)) # (a,b),(x,y)(nx,ny) 모두 좌표
                                    li2[nx][ny]="3" # 3=바이러스에 의해 감염된 곳 2=원래 바이러스의 위치
            
            safezone=0   
            for a in range(0,n):
                for b in range(0,m):
                    if li2[a][b]=="0":
                        safezone+=1
            
            
            answer=max(answer,safezone)

print(answer)
