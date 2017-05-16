T = input()

for i0 in xrange(T):
    max=0
    [n,k]=map(int,raw_input().split())
    for i in range(1,k+1):
        if n%i>max:
            max=n%i
    print max
