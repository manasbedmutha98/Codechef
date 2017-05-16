from itertools import *
import sys
from operator import add
[n,k,p1]=map(int,sys.stdin.readline().split())
s=map(int,sys.stdin.readline().split())
x=sys.stdin.readline()
x=x.replace("?"," ? ")
y=x.split()
#y=map(len,y)
if k>n:
    k=n
if y[-1]!="?":
    del y[-1]

def rotate(s,d):
    return s[-d:]+s[:-d]
 
def kmax():
    l=[s[n:n+k] for n in range(len(s)-(k-1))]
    #l=list(set(map(tuple,l)))
    p=0
    for u in l:
        if p<reduce(add,u):
            p=reduce(add,u)
    return p

for i in y:
    if i=="?":
        print kmax()
    else:
        s=rotate(s,len(i))
