class queue_type:
    def __init__(sefl, elements, front):
        self.elements = elements
        self.front = -1
class MyQueue:
    def __init__(self):
        self.MyQueue = []
    def push(self, x: int) -> None:
        self.MyQueue.append(x)
    def pop(self) -> int:
        n = self.MyQueue[0]
        self.MyQueue.remove(self.MyQueue[0])
        return n
    def peek(self) -> int:
        return self.MyQueue[0]
    def empty(self) -> bool:
        return len(self.MyQueue) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()