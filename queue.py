class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self,item):
        self.queue.append(item)
    def dequeue(self):
        if len(self.queue)<1:
            return None
        return self.queue.pop()
    def display (self):
        print(self.queue)



q=Queue()
q.enqueue(5)
q.enqueue(1)
q.enqueue(8)
q.display()
