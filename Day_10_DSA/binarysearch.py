def binary(arr,x,max,min):
    while min<=max :
        mid=min+(max-min)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]<x:
            min=mid+1   
        else:
            max=mid-1
            
    return -1
arr=[1,2,3,4,5,6,7,8]
x=5
res=binary(arr,x,len(arr)-1,0)
if res==-1:
    print("not found")
else:
    print("found:",res)                