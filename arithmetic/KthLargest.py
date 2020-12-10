# -*- coding: utf-8 -*-
import collections
from typing import List
from queue import PriorityQueue
class KthLargest:
    #https://leetcode-cn.com/problems/kth-largest-element-in-a-stream/submissions/
    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.queue=PriorityQueue(k)
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if self.queue.qsize()<self.k:
            self.queue.put(val)
        else:
            re=self.queue.get()
            if  re<val:
                self.queue.put(val)
            else:
                self.queue.put(re)
        re=self.queue.get()
        self.queue.put(re)
        return re



