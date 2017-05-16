from itertools import *
import sys
from operator import add
[n,k,p]=map(int,sys.stdin.readline().split())
s=map(int,sys.stdin.readline().split())
x=sys.stdin.readline()
x=x.replace("?"," ? ")
y=x.split()
#y=map(len,y)
if k>n:
    k=n
if y[-1]!="?":
    del y[-1]
l=[]    
def rotate(s,d):
    return s[-d:]+s[:-d]
 
def kmax():
    l=[s[n:n+k] for n in range(len(s)-(k-1))]
    p=0
    for i0 in l:
        d=reduce(add,i0)
        if p<d:
            p=d
    """
    for i0 in l:
        if p<i0.count(1):
            p=i0.count(1)
            """
    return p

for i in y:
    if i=="?":
        print kmax()
    else:
        s=rotate(s,len(i))
