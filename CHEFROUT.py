import sys
f=["CC","CE","CS","EE","ES","SS"]
T=input()
for i0 in xrange(T):
    s=sys.stdin.readline()
    s=s[:-1]
    c=True
    i=0
    while i<len(s)-1:
        x=s[i]+s[i+1]
        if x not in f:
            c=not c
            break
        i+=1
    if c:
        print "yes"
    else:
        print "no"
