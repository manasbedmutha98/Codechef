import math
T=input()
for i0 in xrange(T):
    [a,b]=map(int,raw_input().split())
    k=int(math.sqrt(a))
    k*=k
    q=int(math.sqrt(a))
    if q*(q+1)>b:
        q=q*(q-1)
    else:
        q*=q+1
    if q>k:
        print "Bob"
    else:
        print "Limak"
        
        
        
