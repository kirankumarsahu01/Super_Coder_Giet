class student:
    __student__id=None
    __marks=None
    __age=None
    coursedict={1001:25575,1002:15500}
    __course=None
    __fee=None
    def __init__(s,student_id,marks,age,course):
        s.__student_id=student_id
        s.__marks=int(marks)
        s.__age=int(age)
        s.__fee=s.coursedict[course]
    def validate_marks(s):
        if s.__marks>=0 and s.__marks<=100:
            return True
        else:
            return False
    def validate_age(s):
        if s.__age>18:
            return True
        else:
            return False
    def check_qualification(s):
        if s.validate_marks() and s.validate_age() and s.__marks>=65:
            s.discount()
            return True
        else:
            return False
    def discount(s):
        if s.__marks>85:
            s.__fee=s.__fee-(0.25*s.__fee)
    def set_id(s,id):
        s.__student_id=id
    def get_id(s):

        return s.__student_id
    def set_marks(s,marks):
        s.__marks=marks
    def get_marks(s):
        return s.__marks
    def set_age(s,age):
        s.__age=age
    def get_age(s):
        return s.__age
    def get_discount(s):
        return s.__fee
    def display(s):
        print()
        print("id is :",s.__student_id)
        print("age is :",s.__age)
        print("marks is :",s.__marks)
        if s.check_qualification():
            print("qualified")
            print("amount:",s.__fee)
        else:
            print("not qualified")
a=student(101,97,25,1001)
b=student(102,34,25,1002)
c=student(103,84,17,1001)
a.display()
b.display()
c.display()


        
        
        
