class Customer:
    def __init__(s,no) -> None:
        s.__no_of_pizza=no
    def validate_quantity(s):
        if(s.__no_of_pizza>=1 and s.__no_of_pizza<=5):
            return True
        else:
            return False
    def set_no(s,no):
        s.__no_of_pizza=no
    def get_no(s):
        return s.__no_of_pizza


class Pizzaservice:
    count = 100
    def __init__(s,type,customer,topping=False) -> None:
        s.__additional_topping=topping
        s.__size=type
        s.__cost=None
        s.__service_id=None
        s.__customer=customer
        s.calculate_cost()
    def validate_type(s):
        if(s.__size.lower() in ["small","medium"]):
            return True
        else:
            return False
    def calculate_cost(s):
        if(s.__customer.validate_quantity() and s.validate_type()):
            if(s.__size=="small"):
                if(s.__additional_topping):
                    s.__cost=180*s.__customer.get_no()
                else:
                    s.__cost=150*s.__customer.get_no()
                s.generate_service_id()
            elif(s.__size=="medium"):
                if(s.__additional_topping):
                    s.__cost=250*s.__customer.get_no()
                else:
                    s.__cost=200*s.__customer.get_no()
                s.generate_service_id()
        else:
            s.__cost=-1
    def generate_service_id(s):
        Pizzaservice.count+=1
        s.__service_id=s.__size[0]+str(int(s.count))

    def set_topping(s,topping):
        s.__additional_topping=topping
    def get_topping(s):
        return s.__additional_topping
    def set_type(s,type):
        s.__size=type
    def get_type(s):
        return s.__size
    def get_cost(s):
        return s.__cost
    def get_service_id(s):
        return s.__service_id
    def get_customer(s):
        return s.__customer
    
class Doordelivery:
    def __init__(s,distance,pizza) -> None:
        s.__distance=distance
        s.__pizza=pizza
        s.__cost=s.__pizza.get_cost()
        s.calculate_cost()
    def validate_distance(s):
        if(s.__distance>=1 and s.__distance<=10):
            return True
        else:
            return False
    def calculate_cost(s):
        # print(s.__pizza.get_cost())
        if(s.__cost>0):
            if(s.validate_distance()):
                if(s.__distance<=5):
                    s.__cost=s.__cost+(5*s.__distance)
                else:
                    s.__cost=s.__cost+((s.__distance-5)*7)+25
        else:
            s.__cost=-1
    def display(s):
        print()
        print("Service Id: ",s.__pizza.get_service_id())
        print("Number of pizza: ",s.__pizza.get_customer().get_no())
        print("Additional toppings: ",s.__pizza.get_topping())
        print("Distance: ",s.__distance)
        print("cost: ",s.__cost)



c1=Customer(2)
p1=Pizzaservice("medium",c1,True)
p1.calculate_cost()
d1=Doordelivery(10,p1)
d1.calculate_cost()
d1.display()
