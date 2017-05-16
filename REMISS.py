T = input()
M=[]

for i in range (T):
    A, B = map(int,raw_input().split(" "))
    M.append([max (A,B),A+B])
    


for i in range(len(M)):
    for j in range(len(M[i])):
        print M[i][j],
    print
