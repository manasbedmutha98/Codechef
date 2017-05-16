T = input()
def f(x,y):
    c=1
    for i in s:
        if i=="L":
            x-=1
        if i=="D":
            y-=1
        if i=="R":
            x+=1
        if i=="U":
            y+=1

        if abs(x)==m or abs(x)==n:
            c=0
            return c
    return(c)
        
    

for i0 in xrange(T):
    [n,m]=map(int,raw_input().split())
    s=raw_input()
    s=list(s)
    o="safe"
    if f(0,0)or f(m-1,0) or f(m-1,n-1) or f(0,n-1):
        o="unsafe"
    print o
            
            
            
        
