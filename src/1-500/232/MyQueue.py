# O(1) push, O(n) pop
class MyQueue:

    def __init__(self):
        self.s1, self.s2 = [], []
        
    def push(self, x: int) -> None:
        self.s1.append(x)
        
    def pop(self) -> int:
        for i in range(0, len(self.s1) - 1):
            self.s2.append(self.s1.pop())
        temp = self.s1.pop()
        for i in range(0, len(self.s2)):
            self.s1.append(self.s2.pop())
        return temp

    def peek(self) -> int:
        return self.s1[0]

    def empty(self) -> bool:
        return len(self.s1) == 0

# O(1) push, Amortized O(1) pop
class MyQueue_1:

    def __init__(self):
        self.s1, self.s2 = [], []

    def push(self, x):
        self.s1.append(x)

    def pop(self):
        self.peek()
        return self.s2.pop()

    def peek(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]        

    def empty(self):
        return not self.s1 and not self.s2