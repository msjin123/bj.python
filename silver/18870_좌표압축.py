n=int(input())
arr=list(map(int,input().split()))

arr2=[]
# n개의 좌표 각각에 그 좌표의 index 심어놓기
for i in range(0,n):
    arr2.append([arr[i],i]) 

arr2.sort()

ans=0
# 정렬된 좌표를 바탕으로 ans만을 이용해서 좌표 압축하기
for i in range(0,n):
    arr2[i].append(ans)
    if (i!=n-1):
        if (arr2[i+1][0]>arr2[i][0]):
            ans+=1
            
        
            

# 심어놓은 index를 이용해서 정렬하기 전 원래 좌표의 순서로 되돌아가기
arr2.sort(key=lambda x:x[1])

# [[좌표,index,좌표 압축]]
for ar in arr2:
    print(ar[2],end=" ")
