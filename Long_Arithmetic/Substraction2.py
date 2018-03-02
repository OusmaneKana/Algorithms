""" This is my source for the second week assignment of my algorithm class
Lecturer : Mustapha Bedir Tapkan
Autor : Serigne Ousmane Kana Ciss 
Date : January 19 2018"""

"""After Solving this i'll try to use stacks to solve this problem"""


l1=str(input(""))
l2=str(input(""))


#Create an Array to set the biggest the smallest number in a appropriate array
Max=[]
Min=[]


if len(l1)>len(l2):
	for char in l1:
		Max += char
	for char in l2:
		Min += char
else:
	for char in l2:
		Max += char
	for char in l1:
		Min += char
	
result=[0]*(len(Max))
carry=[0]*(len(Min))

carry = False
c=0
i=1

while (len(Min)-c!=0):
# For the substraction operation, the carry gonna be if the number of the bottom is greater than the number on the top .......if i am making sense XD XD

	if int(Max[len(Max)-i]) < int(Min[len(Min)-i]):
		print("Carry alert")
		result[len(result)-i]=int(Max[len(Max)-i])+10- int(Min[len(Min)-i])
		carry = True
		
	else:
		carry = False
		result[len(result)-i]=int(Max[len(Max)-i])- int(Min[len(Min)-i])

	if carry:
		result[len(result)-i-1]=int(Max[len(Max)-i-1])- int(Min[len(Min)-i])+1

	# print(result)
	c+=1
	i+=1
# remaining_count=len(Max)-len(Min)

while (len(Max)-c!=0):
	if carry:
		print("Carry alert from past")
		result[len(result)-i]=int(Max[len(Max)-i])-1
		carry = False
		
	else:
		print("no carry")
		result[len(result)-i]=int(Max[len(Max)-i])

	# Footprint print(result)
	c+=1
	i+=1


StrResult= ''.join(str(e)for e in result)

if int(l1)<int(l2):
	print("Your result of ",l1,"-",l2," is","-", StrResult)
else:
	print("Your result of ",l1,"-",l2," is", StrResult)

# while (len(Max)-c!=0):
# 	pass
