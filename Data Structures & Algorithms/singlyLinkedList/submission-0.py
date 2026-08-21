class LinkedList:

    def __init__(self):
        self.data = [[None, None]]
        self.head = 0
        self.tail = 0
        self.length = 0

    def get(self, i: int) -> int:
        if i < 0 or i >= self.length:
            return -1

        pos = self.data[self.data[self.head][1]]

        for _ in range(i):
            pos = self.data[pos[1]]

        return pos[0]

    def insertHead(self, val: int) -> None:
        new_index = len(self.data)
        self.data.append([val, self.data[self.head][1]])
        self.data[self.head][1] = new_index

        if self.length == 0:
            self.tail = new_index

        self.length += 1

    def insertTail(self, val: int) -> None:
        new_index = len(self.data)
        self.data.append([val, None])

        self.data[self.tail][1] = new_index
        self.tail = new_index
        self.length += 1

    def remove(self, i: int) -> bool:
        if i < 0 or i >= self.length:
            return False

        prev = self.head

        for x in range(i):
            prev = self.data[prev][1]

        target = self.data[prev][1]

        self.data[prev][1] = self.data[target][1]

        if target == self.tail:
            self.tail = prev

        self.length -= 1

        if self.length == 0:
            self.tail = self.head

        return True

    def getValues(self) -> list[int]:
        values = []
        curr = self.data[self.head][1]

        while curr is not None:
            values.append(self.data[curr][0])
            curr = self.data[curr][1]

        return values