import sys
T = int(sys.stdin.readline())
for i0 in xrange(T):
    [x1,y1,x2,y2]=map(int,sys.stdin.readline().split())
    if x1==x2:
        if y1<y2:
            print "up"
        else:
            print "down"
    elif y1==y2:
        if x1<x2:
            print "right"
        else:
            print "left"
    else:
        print "sad"
