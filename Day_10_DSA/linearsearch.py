def linearsearch(arr,n,x):
    for i in range(0,n):
        if arr[i]==x:
            return i
    return -1
arr=[1,2,3,4,5,6,7]
n=len(arr)
x=2
result=linearsearch(arr,n,x)
if result==-1:
    print("not found")
else:
    print("index:",result)

