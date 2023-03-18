class customer:
    def __init__(s,quantity,name):
        s.__quantity=int(quantity)
        s.__name=name
    def validate_quantity(s):
        if s.__quantity>0 and s.__quantity<6:
            return True
        else:
            return False
class pizzaservice:
    count=100
    def __init__(s,additional_toping,type,customer):
        s.__additional_toping=additional_toping
        s.__type=type
        s.__customer=customer
        s.pizzacost=0
        s.__servicce
    def validate_pizza_type(s,type):
        if s.__type=='small':
            return True
        elif s.__type=='medium':
            return True
        else:
            return False
    def calculate_pizza_cost(s):
         if customer.validate_quantity() and s.validate_pizza_type():
             if s.__type=='small':
                 if s.__additional_toping():
                     return customer.__quantity*185
                 else:
                     return customer.__quantity*150
             else:
                if s.__additional_toping():
                    return customer.__quantity*250
                else:
                    return customer.__quantity*200
class doordelivery:
    def __init__(s,distance):
        s.__distance=distance
    def validate_distance_in_kms(a):
        if s.__distance>0 and s._distance<11:
            return True
        else:
            return False
        

                
        
