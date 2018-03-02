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

	if carry:
		#Footprint: print ('Okey with Carry')
		result[len(result)-i+1]-=10
		result[len(result)-i]=int(Max[len(Max)-i])+ int(Min[len(Min)-i])+1
		
	elif not carry:
		#Footprint:  print ('Okey no Carry')
		result[len(result)-i]=int(Max[len(Max)-i])+ int(Min[len(Min)-i])
		
	#Footprint print(result)

	if result[len(result)-i]>=10:
		#Footprint: print("Carry alert")
		carry = True

	else:
		carry = False

	c+=1
	i+=1
# remaining_count=len(Max)-len(Min)
"""At this stage if the Min legnth is over we will just check the next index if there is a carry, we will add 1 and the rest will be field by the rest of max"""

while (len(Max)-c!=0):
	if carry:
		result[len(result)-i]=int(Max[len(Max)-i])+1
		result[len(result)-i+1]-=10
		carry = False
	else:
		result[len(result)-i+1]-=10
		result[len(result)-i]=int(Max[len(Max)-i])
	print(result)
	c+=1


StrResult= ''.join(str(e)for e in result)


#print("The result of ",l1,"+",l2," is", StrResult)
print(StrResult)
# while (len(Max)-c!=0):
# 	pass
