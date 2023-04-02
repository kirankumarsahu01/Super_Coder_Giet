'''def bubblesort(arr,n):
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
arr=[5,3,7,6,2]
n=len(arr)
bubblesort(arr,n)
print(arr)'''
def bubblesort(arr,n):
    for i in range(n):
        for j in range(0,n-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
arr=[5,3,7,6,2]
n=len(arr)
bubblesort(arr,n)
print(arr)                
                       