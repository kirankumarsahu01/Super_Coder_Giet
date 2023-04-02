def update(marks,new_mark,position):
    marks.insert(position,78)
    return marks        
marks=[89,78,99,76,77,67,99,98,90]            
print(update(marks,88,8))
print(marks[5])
print(marks[7])          
