import sys
from itertools import *
from operator import mul
[n,k]=map(int,sys.stdin.readline().split())
s=map(int,sys.stdin.readline().split())
#s.sort()
c=0
for i1 in xrange(1,n+1):
    x= list(combinations( s, i1))
    for i in x:
        p=reduce(mul,i)
        if p>k:
            c+=1
print 2**n-1-c
 
