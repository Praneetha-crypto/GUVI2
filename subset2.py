def isSubset(arr1, arr2, m, n): 
    i = 0
    j = 0
    for i in range(n): 
        for j in range(m): 
            if(arr2[i]==arr1[j]): 
                break  
        if (j==m): 
            return 0
    return 1
m=int(input())      
arr1 =list(map(int,input().split()))
n=int(input())
arr2 = list(map(int,input().split()))
#m = len(arr1) 
#n = len(arr2)   
if(isSubset(arr1, arr2, m, n)==1): 
    print("Yes ") 
else: 
    print("No") 
  
