T = input()
A = []

for i in range (T):
    N = input()
    S = N
    R = 0
    while N>0:
        R=10*R+(N%10)
        N=N/10
    
    if S==R:
        A.append("wins")
    else:
        A.append("losses")
    
        
for x in A:
    print x
