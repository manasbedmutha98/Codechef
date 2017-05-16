T=input()

for i0 in xrange(T):
    A="YES"
    n=input()
    a=raw_input().split()
    if a[-1]=="cookie":
        A="NO"
    else:
        for i in range(len(a)-1):
            if a[i]=="cookie" and a[i+1]!="milk":
                A="NO"
                break

    print A
            
