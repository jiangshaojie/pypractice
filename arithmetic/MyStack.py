# -*- coding: utf-8 -*-
import collections
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queque=collections.deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queque.append(x)
        size=len(self.queque)
        index=1
        while index<size:
            index=++index
            self.queque.append(self.queque.pop())

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queque.pop()

    def top(self) -> int:
        """
        Get the top element.
        """
        item=self.queque.pop()
        self.queque.appendleft(item)
        return item

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not bool(self.queque)



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
