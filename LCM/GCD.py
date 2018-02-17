
def GCD(a,b):
	while (a!=0 and b!= 0):
		mx=max(a,b)
		mn=min(a,b)
		a = mx%mn
		b = mn
	return b
def LCM():
	c = GCD()
	

