class MyQueue:
    def __int__(self):
        self.instack = []
        self.outstack = []

    def push(self, value):
        self.instack.append(value)

    def pop(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack[-1]

    def empty(self):
        return len(self.instack) == 0 and len(self.outstack) == 0