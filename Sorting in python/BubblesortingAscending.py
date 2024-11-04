arr=[6,2,3,9,5]
for i in range(len(arr)-1):
    for j in range(len(arr)-i-1):
        if(arr[j]>arr[j+1]): 
            arr[j],arr[j+1]= arr[j+1],arr[j]


print(arr)


arr=[8,3,4,6,10]

for i in range(len(arr)-1):
    for j in range(len(arr)-i-1):
        if(arr[j]<arr[j+1]):
            arr[j], arr[j+1]= arr[j+1],arr[j]

            print(arr)