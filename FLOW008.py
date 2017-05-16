T = input()
A=[]

for i in range (T):
    N = input()
    if N<10:
        A.append("What an obedient servant you are!")
    else:
        A.append("-1")

for x in A:
    print x

