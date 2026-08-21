class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = [None]*capacity
        self.back = 0

    def get(self, i: int) -> int:
        return self.data[i]

    def set(self, i: int, n: int) -> None:
        self.data[i] = n

    def pushback(self, n: int) -> None:
        if self.back == self.capacity:
            self.resize()
        self.data[self.back] = n
        self.back = self.back + 1
        

    def popback(self) -> int:
        self.back = self.back - 1
        popped = self.data[self.back]
        self.data[self.back] = None
        return popped

    def resize(self) -> None:
        self.data = self.data + [None]*self.capacity
        self.capacity = self.capacity * 2

    def getSize(self) -> int:
        return self.back
    
    def getCapacity(self) -> int:
        return self.capacity