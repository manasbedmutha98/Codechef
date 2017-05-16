T = input()
A = []

for i in range(T):
    N = input()
    L=[]
    for i in range(N):
        L.append(input())
    L.sort()
    i=0
    while(len(L)>1):
        if L[i]==L[i+1]:
            del L[i]
            del L[i]
    A.append(L[0])
for x in A:
    print x

