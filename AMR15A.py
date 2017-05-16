N = input()
A=[]

L=map(int,raw_input().split(" "))
odd=0
even=0

for x in L:
    if(x%2==1):
        odd+=1
    else:
        even+=1

if(even>odd):
    print "READY FOR BATTLE"
else:
    print "NOT READY"

