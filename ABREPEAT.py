T = input()
for i0 in xrange(T):
    [n,k] = map(int,raw_input().split())
    s=raw_input()
    s*=k
    i=0
    c=0
    while i<(n*k)-1:
        h=s.index("a",i+1)
        j=h
        while j<n*k-1:
            m=s.index("b",j+1)
            c+=1
            j=m
        i=h
    print c
