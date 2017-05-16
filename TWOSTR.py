T = input()
A = []

for i in range (T):
    a = raw_input()
    b = raw_input()
    c=0
    for j in range (len(a)):
        if (a[j]!="?" and b[j]!="?") and a[j]!=b[j]:
            c=1
            break
    A.append(c)

for i in A:
    if c==1:
        print "No"
    else:
        print "Yes"
            
            
