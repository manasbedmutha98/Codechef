T = input()
A=[]

for i in range (T):
    S = input()
    Sal = 0
    if S<1500:
        Sal = 2.0*S
    else:
        Sal = S + 500 + (0.98*S)

    A.append(Sal)

for x in A:
    print x
