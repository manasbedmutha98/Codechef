T = input()
A = []

for i in range (T):
    a,b=map(int,raw_input().split(" "))
    t=0
    while b!=a:
        if b>a:
            a=2*a
            t+=1
        if a>b:
            if a%2==1:
                a=(a-1)/2
            else:
                a = a/2
            t+=1
    A.append(t)

for x in A:
    print x
