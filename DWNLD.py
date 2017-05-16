t = input()
while(t):
    n,k=map(int,raw_input().split())
    sum=0
    cost=0
    di=0
    c=0
    while(sum<k):
        ti,di=map(int,raw_input().split())
        sum+=ti
        c+=1
    if (sum-k)>0:
        cost+=(di*(sum-k))
        
    for i in range(n-c):
        ti,di=map(int,raw_input().split())
        cost+=(di*ti)
    print cost

    t-=1
        
        
        
    
