t = int(input())
while(t):
	n = int(input())
	if (n%2==0):
		# tot pal are 10**(n/2)
		# tot comb are 10**n, ans is 10**(n/2)
		ans = "1 1"+"0"*(n//2)
	else:
		# tot pal are 10**((n+1)/2), tot comb are 10**(n+1)
		ans = "1 1"+"0"*((n-1)//2)
	print (ans)


	t-=1