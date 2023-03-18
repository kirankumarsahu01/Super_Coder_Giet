def strings(n1,n2):
    a=[]
    for i in n1:
        if i in n2:
            a.append(i)
    if a==[]:
        return -1
    else:
        return a
print(strings("ilikePython","javaisverypopularlanguage"))    
            
