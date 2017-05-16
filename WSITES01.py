import sys
T=int(sys.stdin.readline())
A=[]
B=[]
C=[]
for i0 in xrange(T):
    s=sys.stdin.readline()
    if s[0]=="+":
        A.append(s.split()[1])
    else:
        B.append(s.split()[1])
for i in A:
    for j in B:
        for k in range(len(j)):
            if (j[:k] not in i):
            #and (j[:k] not in C):
                C+=[j[:k]]
                break
        
      
    
C.sort()
for i in range(len(C)):
    for j in range(i+1,len(C)):
        if C[i] in C[j]:
            C[i]=""
#C.remove("")
C=filter(lambda a: a != "", C)
if len(C)==0:
    print -1
else:
    print len(C)
    for i0 in C:
        print i0
