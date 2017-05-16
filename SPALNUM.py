T = input()

A=[]
def pal(n):
    N=str(i)
    M=N[::-1]
    if N==M:
        return True
    else:
        return False
    
for k in range (T):
    L, R = map(int, raw_input().split(" "))
    S=0
    for i in range (L,R+1):
        if pal((i)):
            S+=i
    A.append(S)

for x in A:
    print x
        
