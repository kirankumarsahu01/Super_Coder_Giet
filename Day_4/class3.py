#ID OF THE OBJECT

class Shoe:
    def __init__(self,price,material):
        self.price=price
        self.material=material

s1=Shoe(1000,"canvas")
print("the unique id of the object ",id(s1))
s2=Shoe(1000,"canvas")
print("the unique id of the object ",id(s2))
#use of default function will return address
class Shoe:
    def __init__(self,price,material):
        self.price=price
        self.material=material

s1=Shoe(1000,"canvas")
print(s1)


#str function will work as we have chnaged the default
class Shoe:
    def __init__(self,price,material):
        self.price=price
        self.material=material
    def __str__(self):
        return "shoe with price:"+str(self.price)+"and material:"+self.material
s3=Shoe(1000,"canvas")
print(s3)  

