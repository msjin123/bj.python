n=int(input())

arr=list(map(int,input().split()))

dic={}
start=0
end=0
sum=-1 #길이
answer=0
dic[arr[0]]=1

while(end<n):
    sum=len(dic)
    if (sum<3):
        end+=1
        # -----------
        # 끝까지 갔을때 answer 갱신하고 종료
        if (end==n): 
            answer=max(answer,end-start)
            break
        # -----------        
        if (arr[end] not in dic):
            dic[arr[end]]=1
        else:
            dic[arr[end]]+=1

        
    elif (sum==3):
        
        answer=max(answer,end-start)
        dic[arr[start]]-=1
        if (dic[arr[start]]==0):
            dic.pop(arr[start])
        start+=1

print(answer)
