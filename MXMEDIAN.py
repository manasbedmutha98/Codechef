T=input()
for i0 in xrange(T):
    n=input()
    s=map(int,raw_input().split())
    s.sort()
    print s[(3*n-1)/2]
    for i in range(n):
        print s[i],
        print s[n+i],
    print ""
