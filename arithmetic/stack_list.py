# -*- coding: UTF-8 -*-

def isValid(self, s: str) -> bool: #https://leetcode-cn.com/problems/valid-parentheses/\
    """
    not in 可以用来判定item 是否在list，map 中。not x 可以用来判断 list map 是否为空
    :param self:
    :param s:
    :return:
    """
    stack = []
    # paren_map={"(":")","{":"}","[":"]"}
    paren_map = {")": "(", "}": "{", "]": "["}
    for a in s:
        # if paren_map.get(a) is None:
        if a not in paren_map:
            stack.append(a)
        elif not stack or paren_map.get(a) != stack.pop():
            return False
    return not stack

class MyQueue:   #https://leetcode-cn.com/problems/implement-queue-using-stacks/submissions/

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.input.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        if not self.output:
            return None
        else:
            return self.output.pop()


    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        if not self.output:
            return None
        else:
            return self.output[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return not bool(self.output)


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
print(obj)
param_2 = obj.pop()
print(param_2)
param_3 = obj.peek()
print(param_3)
param_4 = obj.empty()
print(param_4)
