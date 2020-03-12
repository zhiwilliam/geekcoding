# Solution using List - O(1) push, O(n) pop
class MyStackList:

    def __init__(self):
        self.list = []

    def push(self, x: int) -> None:
        self.list.append(x)

    def pop(self) -> int:
        return self.list.pop(len(self.list) - 1)

    def top(self) -> int:
        return self.list[len(self.list) - 1]

    def empty(self) -> bool:
        return len(self.list) == 0


# Solution using Queue O(1) push, O(n) pop
from queue import Queue
class MyStackQueue:

    def __init__(self):
        self.q = Queue()

    def push(self, x: int) -> None:
        self.q.put(x)

    def pop(self) -> int:
        for i in range(0, self.q.qsize() - 1):
            self.q.put(self.q.get())
        return self.q.get()

    def top(self) -> int:
        for i in range(0, self.q.qsize() - 1):
            self.q.put(self.q.get())
        temp = self.q.get()
        self.q.put(temp)
        return temp

    def empty(self) -> bool:
        return self.q.empty()


# Slightly faster solution if top() is used frequently
from queue import Queue
class MyStackQueueWithTop:

    def __init__(self):
        self.q = Queue()
        self.t = None
        
    def push(self, x: int) -> None:
        self.q.put(x)
        self.t = x
        
    def pop(self) -> int:
        for i in range(0, self.q.qsize() - 1):
            self.push(self.q.get())
        return self.q.get()
    
    def top(self) -> int:
        return self.t
    
    def empty(self) -> bool:
        return self.q.empty()