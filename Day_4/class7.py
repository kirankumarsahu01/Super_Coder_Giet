class dam:
    def __init__(self,name,length):
        self.name=name
        self.__length=length
    def get_length(self):
        return self.__length
dam1=dam("abc dam",3.5)
print("dam name:",dam1.name)
print("dam length",dam1.get_length())

