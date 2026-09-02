n=int(input())

used_col = [False]*(n+1)
used_diag1 = [False]*(2*n+1)
used_diag2 = [False]*(2*n+1)
ans=0


def recur1(y):
    global ans
    if y==n+1:
        ans+=1
        return 0
    
    for col in range(1,n+1):
        if used_col[col]==True:
            continue
        if used_diag1[col+y]==True:
            continue
        if used_diag2[col-y+n]==True:
            continue
        
        # 퀸 배치
        used_col[col] = True
        used_diag1[col+y] = True      # 오르막 대각선 /
        used_diag2[col-y+n] = True  # 내리막 대각선 \
        recur1(y+1)
        # 백트래킹
        used_col[col] = False
        used_diag1[col+y] = False        
        used_diag2[col-y+n] = False

recur1(1)

print(ans)






