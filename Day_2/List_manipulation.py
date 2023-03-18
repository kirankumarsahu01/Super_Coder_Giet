#list
list1=[]
print(list,type(list))
list2=[10,20.0,"kiran",2+3j]
print(list2)
list4=list([10,20,30])
print(list4)

#append
list4.append(40)
print(list4)
#extends
list4.extend([50,60,70])
print(list4)
list4=list4+[80,90,100]
print(list4)

#insert

list4.insert(1,80)
print(list4)

#remove value
list4.remove(80)
print(list4)

#pop uses index
list4.pop(0)
print(list4)
list4.pop()
print(list4)#last value

#delete
del list4[1]
print(list4)

list3=list(["A","B","C","D"])
print(list3)


