t = input()
ma=0
win=0
while(t):
    a,b=map(int,raw_input().split())
    if (b-a)>0 and (b-a)>ma:
        ma=b-a
        win=2
    elif b<a and a>ma+b:
        ma=a-b
        win=1
    
    t-=1
        
print win,ma
