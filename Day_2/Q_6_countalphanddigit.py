n=input()#enter letter in cap

list4=list(n)
print(list4)
list3=list(["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"])
print(list3)
list2=list(["1","2","3","4","5","6","7","8","9","0"])
print(list2)
count1=0
count2=0
print(list4)
for i in list4:
    if i in list3:
        count1=count1+1
    if i in list2:
        count2=count2+1
print(list[count1,count2])    
    
        
 
