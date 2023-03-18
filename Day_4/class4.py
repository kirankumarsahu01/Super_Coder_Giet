class Mobile:
    def __init__(self):
        print(id(self))
    def display(self):
        print("displaying details")
    def purchase(self):
        self.display()
        print("calculating price")
Mobile().purchase()        
