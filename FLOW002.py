T = input()

M=[]

for i in range (T):
    A, B = map(int,raw_input().split(" "))
    M.append(A%B)

for x in M:
    print x
