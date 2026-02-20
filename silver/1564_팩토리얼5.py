def find_digits(n):
    num=n
    ans=0
    while (num>0):
        num=num//10
        ans+=1
    return ans


import math as m
n=int(input())

# print(m.factorial(9)) = 362880
num=36288
for a in range(10,n+1):
    num=num*a
    

    if (a%(5**8)==0):
        num=num//10**8
        
    elif (a%(5**7)==0):
        num=num//10**7
        
    elif (a%(5**6)==0):
        num=num//10**6
        
    elif (a%(5**5)==0):
        num=num//10**5
        
    elif (a%(5**4)==0):
        num=num//10**4
        
    elif (a%(5**3)==0):
        num=num//10**3
        
    elif (a%(5**2)==0):
        num=num//10**2
        
    elif (a%5==0):
        num=num//10
        
    
    num=num%10**30
    
    # print(a,num)
    # print(a,m.factorial(a))

if (num>100000):
    num=num%10**5  # 5자리로 만들기
    print('0'*(5-find_digits(num))+str(num))
    
else:
    print('0'*(5-find_digits(num))+str(num))
