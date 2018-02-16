def modexpo(x,n,m):
	if (n==0):
		return 1
	if (n%2==0):
		return modexpo(x*x, n/2, m) %m
	if (n%2==1):
		return (x%m)* modexpo(x*x, (n-1)/2, m)%m
	 

print(modexpo(2, 7, 5))