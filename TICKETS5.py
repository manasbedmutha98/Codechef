T = input()
A = []

for i in range (T):
    S = raw_input()
    l =len(S)
    L=[]
    for i in range (l):
        L.append(S[i])
    L.sort()
    while len(L)>2:
        if L[i]==L[i+1]:
            del L
        
