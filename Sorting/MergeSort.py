
def MergeArrays(arr, l, m, r):
    n1 = m - l + 1
    n2 = r- m
 
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
 
   
    for i in range(0 , n1):
        L[i] = arr[l + i]
 
    for j in range(0 , n2):
        R[j] = arr[m + 1 + j]
 
   
    i = 0     
    j = 0     
    k = l     
 
    while i < n1 and j < n2 :
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
   
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
 

def Sorting(arr,l,r):
    if l < r:
 
    
        m = int((l+(r-1))/2)

        Sorting(arr, l, m)
        Sorting(arr, m+1, r)
        MergeArrays(arr, l, m, r)
 
 
arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print ("\nBefore Sorting")
for i in range(n):
    print ("%d" %arr[i])


Sorting(arr,0,n-1)
print ("\nAfter Sorting")
for i in range(n):
    print ("%d" %arr[i])
 