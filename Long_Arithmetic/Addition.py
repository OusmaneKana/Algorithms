""" This is my source for the second week assignment of my algorithm class
Lecturer : Mustapha Bedir Tapkan
Autor : Serigne Ousmane Kana Ciss 
Date : January 19 2018"""

#Create two array/list to store the two operands

l1="99"
l2="99"

lenght = max(len(l1),len(l2))+1
result=[0]*(lenght)
carry=[0]*(lenght)

i = 1
while (min(len(l1),len(l2))-i+1>=0):
	if carry[lenght-i]==0:
		result[lenght-i] = int(l1[len(l1)-i]) + int(l2[len(l2)-i])

		print ("ok",result)
	else :
		
		result[lenght-i] = int(l1[len(l1)-i]) + int(l2[len(l2)-i])+1

		print ("bn",result)
	
	if result[lenght-i] >=10:
		result[lenght-i]-=10
		carry[lenght-(i+1)]=1

	i+=1
	
	current_lenght = (max(len(l1),len(l2))-min(len(l1),len(l2)))-1

# while current_lenght>=0:
# 	if carry[lenght-i]==1:
# 		if (l1>l2):
# 			result[current_lenght]=int(l1[current_lenght])+1
# 		else:
# 			result[current_lenght]=int(l2[current_lenght])+1
# 		print ("Still have a carry")
# 	else:
# 		if (l1>l2):
# 			result[current_lenght]=int(l1[current_lenght])
# 		else:
# 			result[current_lenght]=int(l2[current_lenght])
# 		print ("Still have a carry")
 
# 	current_lenght-=1
# 	i+=1



print(result)

