T = input()

M=[]

for i in range (T):
    S = raw_input()
    A = int(S[0])
    B = int(S[len(S)-1])
    M.append(A+B)

for x in M:
    print x
