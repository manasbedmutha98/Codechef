t= input()
for i in range(t):
    c=0
    a=raw_input().split()
    b=raw_input().split()
    
    for i in a:
        if i in b:
            c+=1
    if c>=2:
        print "similar"
    else:
        print "dissimilar"
    
