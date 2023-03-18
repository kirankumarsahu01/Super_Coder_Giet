def num(n):
    m=2*n
    x=str(m)
    y=str(n)
    if len(x)==len(y):
        for i in x:
            if(i not in y):
                return False
        else:
            return True
    else:
        return False
            


print(num(125874))    
