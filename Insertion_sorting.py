def selection_sorting(arr):
     for i in range(0,len(arr)):
          j=i
          while arr[j-1]>arr[j] and j>0:
               arr[j-1], arr[j]=arr[j],arr[j-1]
               j-=1

arr=[2,5,6,8,9]
selection_sorting(arr)
print(arr)