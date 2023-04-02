def check_anagram(str1,str2):
    l1=list(str1)
    l2=list(str2)
    if len(l1)==len(l2):
        for i in l1:
            if i in l2:
                if str1!=str:
                    return True
    return False
print(check_anagram('anagram','ramnaga'))            
        