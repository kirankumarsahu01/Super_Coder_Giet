class vechile:
    def __init__(s):
        s.__id=None
        s.__type=None
        s.__cost=None
        s.__amount=None
    def cal_premium(s,type):
        if(type=='two wheeler'):
            s.__amount=int(s.__cost)*0.02
        elif(type=='four wheeler'):
            s.__amount=int(s.__cost)*0.06
    
    def get_id(s):
        return s.__id
    def set_id(s,id):
        s.__id=id
    def get_cost(s):
        return s.__cost
    def set_cost(s,cost):
        s.__cost=cost
    def get_type(s):
        return s.__type
    def set_type(s,type):
        if type=='two wheeler':
            s.__type=type
        elif type=='four wheeler':
            s.__type=type
        else:
            s.__type='error'
    def get_premium(s):
        return s.__amount
    def display(s):
        print(s.__id)
        print(s.__cost)
        print(s.__type)
        print(s.__amount)

s1=vechile()
id=input()
cost=input()
type=input()
s1.set_id(id)
s1.set_cost(cost)
s1.set_type(type)
s1.cal_premium(type)
print(s1.get_id())
print(s1.get_cost())
print(s1.get_type())
print(s1.get_premium())
s1.display()

        
        
        
        
        
