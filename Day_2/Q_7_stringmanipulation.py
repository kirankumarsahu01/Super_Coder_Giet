def str(a):
    if len(a)<3:
        return a
    else:
        if a[-3:]!="ing":
            return a+"ing"
        else:
            return a+"ly"
print(str("kiraning"))        
        
    
            
            
