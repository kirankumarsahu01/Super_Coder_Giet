#currency converter
def con(cur,amount):
    if cur=="Euro":
        return amount*0.01417
    elif cur=="British Pound":
        return amount*0.0100
    elif cur=="Australian Dollar":
        return amount*0.02140
    elif cur=="Canadian Dollar":
        return amount*0.2027
    else:
        return -1
print(con("Euro",300))    
            

    

    

    

    

        
