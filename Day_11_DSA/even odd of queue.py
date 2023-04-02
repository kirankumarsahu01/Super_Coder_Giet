class queue:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__list=[None]*max_size
        self.__rare=-1
        self.__front=0
    def is_empty(self):
        if self.__rare<self.__front:
            return True
        else:
            return False
    def is_full(self):
        if self.__rare==self.__max_size-1:
            return True
        return False
    def enqueue(self,data):
        if self.is_full():
            print("queue is full")
        else:
            self.__rare+=1
            self.__list.insert(self.__rare,data)
    def dequeue(self):
        if self.is_empty():
            print("empty")
        else:
            x=self.__list[self.__front]
            self.__list[self.__front]=None
            self.__front+=1
            return x
    def display(self):
        for i in range(self.__front,self.__rare+1):
            print(self.__list[i],end=" ")
    def get_maxsize(s):
        return s.__max_size
            
            
def evenodd(q):
    qe=queue(q.get_maxsize())
    qo=queue(q.get_maxsize())
    for i in range(q.get_maxsize()):
        x=q.dequeue()
        if(x%2==0):
            qe.enqueue(x)
        else:
            qo.enqueue(x)
    qe.display()
    print()
    qo.display()
            
                
            
q=queue(10)
l=[int(i) for i in range(1,11)]
for i in l:
    q.enqueue(i)
evenodd(q)
# q.display()
       
        
            
                   