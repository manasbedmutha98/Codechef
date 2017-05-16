T = input()

for i0 in xrange(T):
    A={}
    [n,k]=map(int,raw_input().split())
    a=map(int,raw_input().split())
    for i in range(len(a)):
        if a[i]!=i+1:
            A[a[i]]=A.get(a[i]+1,1)
        else:
            ao=a.pop(i)
            i+=1
    B=0
    for i in A.keys():
        if i>=k:
            B+=1

    print B
            
                
        
