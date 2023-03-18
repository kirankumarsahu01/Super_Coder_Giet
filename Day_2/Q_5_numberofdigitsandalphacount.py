n=input()
count1=0
count2=0
for i in n:
    if i.isalpha():
        count1=count1+1
    elif i.isdigit():
        count2=count2+1
    else:
        continue
l=[count1,count2]
print(l)

    
