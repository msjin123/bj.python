import sys
input=sys.stdin.readline
# from queue import PriorityQueue
import heapq
n=int(input().strip())
q1=[]
for _ in range(n):
    num=int(input().strip())
    
    if (num!=0): # (절댓값,원래값)
        if (num>0):
            # q1.put((num,num))
            heapq.heappush(q1,(num,num))
        elif (num<0):
            heapq.heappush(q1,(-num,num))
    else:
        if (len(q1)==0):
            print(0)
        else:
            print(heapq.heappop(q1)[1])
