def strings(n1,n2):
    l=[]
    for i in range(0,len(n1)):
        for j in range(0,len(n2)):
            if n1[i]==n2[j]:
                l.append(n1[i])
    if l==[]:
        return -1
    else:
        return l
print(strings("kiran","nayan"))            
                
                
