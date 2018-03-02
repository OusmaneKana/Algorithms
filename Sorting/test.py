

def DivideArr(arr):
	m = int(len(arr)/2)
	R = arr[m:]
	L = arr[:m]
	DivideArr(R)
	DivideArr(L)
	print ("OK BOn")

	




def Merge():
	DivideArr(arr = [9,3,7,31,5,34,56,4,32,3])



	