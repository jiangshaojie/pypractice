# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        windows = []
        res = []
        for i, x in enumerate(nums):
            if i >= k and windows[0] <= i - k:
                windows.pop(0)
            while windows and nums[windows[-1]] <= x:
                windows.pop()
            windows.append(i)
            if i >= k - 1:
                res.append(nums[windows[0]])
        return res

    def maxSlidingWindow1(self, nums: List[int], k: int) -> List[int]:
        pass

    def isAnagram(self, s: str, t: str) -> bool:
        # #https: // leetcode - cn.com / problems / valid - anagram / submissions /
        return sorted(s)==sorted(t)
    def isAnagram_map(self,s:str,t:str) -> bool:
        dic1={}
        dic2={}
        for item in s:
            dic1[item]=dic1.get(item,0)+1
        for item in t:
            dic2[item]=dic2.get(item,0)+1
        return dic1==dic2
    def isAnagram_map_1(self,s:str,t:str)->bool:
        dic1=[0]*26
        dic2=[0]*26
        for item in s:
            dic1[ord(item)-ord("a")]+=1
        for item in t:
            dic2[ord(item)-ord("a")]+=1
        return dic1==dic2





