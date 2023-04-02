def checkdouble(list1,list2):
    new_list=[]
    for i in list1:
        if i*2 in list2:
            new_list.append(i)
    return new_list
list1=[11,8,23,7,25,15]
list2=[6,33,50,31,46,78,16,34] 
print(checkdouble(list1,list2))       