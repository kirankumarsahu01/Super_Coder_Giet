sen=["a new world record was set",
     "in the holy city of ayodhya",
     "on the eve of diwali on tuesday",
     "with over three lakhs of diya or earthen lamps",
     "lit up simuntanously on the bank of the sarayu river"]
stopwords=["for","a","of","the","and","to","in","on","with","was","or"]
ans=[]
for i in sen:
    for j in i.split():
        if j not in stopwords:
            ans.append(j)
print(ans)            
print(" ".join(ans))
l=[j for j in i.split() for i in sen if j not in stopwords]
print(l)

         
