def selectionsort(arr,s):
    for step in range(s):
        min_ind=step
        for i in range(step+1,s):
            if arr[i]<arr[min_ind]:
                min_ind=i
        (arr[step],arr[min_ind])=(arr[min_ind],arr[step])
data=[1,2,3,4,5,6,0]
s=len(data)
selectionsort(data,s)
print(data)
            
                