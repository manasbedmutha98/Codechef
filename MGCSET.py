# your code goes here
t = int(input())
while(t):
    n, m = map(int,input().split())
    arr = map(int,input().split())
    c = 0
    for i in arr:
        if i%m == 0:
            c += 1
    print((2**c)-1)
    t -= 1
    # your code goes here# your code goes here