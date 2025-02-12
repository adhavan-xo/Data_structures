class myCriculaerQueue():


    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1
    def enqueue(self , data):
        if (self.tail + 1) % self.k == self.head:
            print("Already full")
        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
            print(data)
        else:
            self.tail == (self.tail + 1) % self.k
            self.queue[self.tail] = data
            print(data)
    def dequeue(self):
        if(self.head == -1):
            print("Queue is empty")
        elif (self.head == self.tail):
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
    def printQueue(self):
        if(self.head == -1):
            print("Queue is empty")
        elif (self.head >= self.tail):
            for i in range (self.head , self.tail +1):
                print(self.queue[i],end=" ")
                print(end=" ")
        else:
            for i in range (self.head , self):
                print(self.queue[i],end=" ")
            for i in range (0,self.tail +1):
                print(self.queue[i],end=" ")
                print(end=" ")




obj = myCriculaerQueue(5)
obj.enqueue(7)
obj.enqueue(9)
obj.enqueue(10)
obj.enqueue(8)
obj.enqueue(0)
obj.enqueue(0)
obj.enqueue(0)
obj.dequeue()
obj.printQueue()