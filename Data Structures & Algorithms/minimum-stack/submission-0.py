class MinStack:
    def __init__(self):
        self.MinStack = []
    def push(self, val: int) -> None:
        self.MinStack.append(val)
    def pop(self) -> None:
        self.MinStack.pop()
    def top(self) -> int:
        return self.MinStack[-1]
    def getMin(self) -> int:
        if len(self.MinStack) != 0 :
            min_value = min (x for x in self.MinStack)
            return min_value
