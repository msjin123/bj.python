snum=input()

len1=len(snum)

if len1%2!=0:
    print(-1)


else:
    judge=True

    inverse=[]
    a=0
    while a!=len1:
        n1=int(snum[a])
        n2=int(snum[a+1])
        # if n1==0:
        #     judge=False
        for i in range(n1):
            inverse.append(n2)      
        a+=2

    len2=len(inverse)     
    
    origin=[]
    b=0
    cnt=0
    num2=-1
    game=False
    # judge=True
    while b!=len2:
        if game==False:  # 처음 다른 숫자
            num2=inverse[b]
            game=True
            cnt+=1 # cnt=1
            b+=1
        else:
            if inverse[b]==num2:
                cnt+=1
                b+=1
            elif inverse[b]!=num2:
                # if cnt>=10:
                #     judge=False
                origin.append(cnt)
                origin.append(num2)
                cnt=0
                game=False
        

    origin.append(cnt)
    origin.append(num2)

    # print(inverse)
    # print(origin)
    len3=len(origin)
    # judge=True
    for i in range(0,len1):
        if i>=len3:
            judge=False
            break
        if int(snum[i])!=origin[i]:
            judge=False
            break

    if inverse[0]==0:  # x>0인 정수에서만 f가 정의
        judge=False

    if (judge):
        # print(*inverse)
        for t in inverse:
            print(t,end='')
    else:
        print(-1)

#

