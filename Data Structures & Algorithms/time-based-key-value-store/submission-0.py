class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.data:
            self.data[key].append((value,timestamp))
        else:
            self.data[key] = [(value,timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""
        arr = self.data[key]
        lower, upper = 0, len(arr) - 1
        result = ""
        while lower <= upper:
            middle = lower + (upper - lower) // 2
            if arr[middle][1] <= timestamp:
                result = arr[middle][0]
                lower = middle + 1
            else:
                upper = middle - 1
        return result
