""" This is my source for the second week assignment of my algorithm class
Lecturer : Mustapha Bedir Tapkan
Autor : Serigne Ousmane Kana Ciss 
Date : January 19 2018"""

"""After Solving this i'll try to use stacks to solve this problem"""
arr1 = str(input(""))
arr2 = str(input(""))
reslt = [0]*5
i=1
j =1
count = len(arr1)

for char in arr1:
	while count != 0:
		print(i,"Th multiplication")
		reslt [len(reslt)-i]= int(arr2[len(arr2)-j])*int(arr1[len(arr1)-i])
		count -=1
		i+=1
	j+=1
	count = len(arr1)

		
print(reslt)			
