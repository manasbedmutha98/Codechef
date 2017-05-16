T = input()
A = []

for i in range(T):
    l,b=map(int,raw_input().split(" "))
    c=0
    while min(l,b)>1:
        m=max(l,b)
        n=min(l,b)
        l=m-n
        b=n
        c+=1
    A.append(2*c)

for x in A:
    print x
        
