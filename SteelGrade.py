T = input()
A=[]

for i in range (T):
    H, C, S = map(float, raw_input().split(" "))
    t1=False
    t2=False
    t3=False

    if H>50:
        t1=True
    
    if C<0.7:
        t2=True
    
    if S>5600:
        t3=True

    grade=0
    if t1 and t2 and t3:
        grade=10
    elif t1 and t2:
        grade=9
    elif t2 and t3:
        grade=8
    elif t1 and t3:
        grade=7
    elif t1 or t2 or t3:
        grade=6
    else:
        grade=5

    A.append(grade)

for i in A:
    print i
