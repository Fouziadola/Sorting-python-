def selection_sor(arr):
    for i in range(0,len(arr)-1):
        min_index=i
        for j in range(i+1,len(arr)):
            if arr[j]>arr[min_index]:
                min_index=j

                arr[i],arr[min_index]=arr[min_index],arr[i]

arr=[3,5,7,9,10,2]
selection_sor(arr)
print(arr)