class MinStack:

    def __init__(self):
        self.data = []
        self.aux_stack = []
        
    def push(self, val: int) -> None:
        self.data.append(val)
        if len(self.aux_stack) == 0 or val < self.aux_stack[-1]:
            self.aux_stack.append(val)
        else:
            self.aux_stack.append(self.aux_stack[-1])

    def pop(self) -> None:
        self.aux_stack.pop()
        return self.data.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.aux_stack[-1]
