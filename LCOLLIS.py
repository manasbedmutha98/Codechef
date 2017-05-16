B=[]    
T = input()
for i in range(T):
    N,M=raw_input().split()
    N = int(N)
    M = int(M)
    S=0
    for i in range(N):
        x = map(int,list(raw_input()))
        s=0
        for i in  range(M):
            if x[i]==1:
                s+=1
        if s>=2:
            S+=(s*(s-1))/2
    B.append(S)

for x in B:
    print x
        
        
