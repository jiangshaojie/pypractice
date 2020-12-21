# -*- coding: utf-8 -*-
from typing import List
from arithmetic.util.TreeNode import TreeNode


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
        return sorted(s) == sorted(t)

    def isAnagram_map(self, s: str, t: str) -> bool:
        dic1 = {}
        dic2 = {}
        for item in s:
            dic1[item] = dic1.get(item, 0) + 1
        for item in t:
            dic2[item] = dic2.get(item, 0) + 1
        return dic1 == dic2

    def isAnagram_map_1(self, s: str, t: str) -> bool:
        dic1 = [0] * 26
        dic2 = [0] * 26
        for item in s:
            dic1[ord(item) - ord("a")] += 1
        for item in t:
            dic2[ord(item) - ord("a")] += 1
        return dic1 == dic2

    def twoSum(self, nums: List[int], target: int) -> list[int]:
        # https://leetcode-cn.com/problems/two-sum/
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return [0]

    def twoSum1(self, nums: List[int], target: int) -> list[int]:
        map = dict()
        for index, item in enumerate(nums):
            if (target - item) in map:
                return [map.get(target - item), index]
            map[item] = index
        return [0]

    def threeSum(self, nums: List[int]) -> List[List[int]]:  # https://leetcode-cn.com/problems/3sum/
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        temp = [nums[i], nums[j], nums[k]]
                        if temp not in res:
                            res.append(temp)
        return res

    def threeSum1(self, nums: List[int]) -> List[List[int]]:  # https://leetcode-cn.com/problems/3sum/
        n = len(nums)
        nums.sort()
        res = []
        for first in range(n):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            third = n - 1
            for second in range(first + 1, n):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                while second < third and nums[first] + nums[second] + nums[third] > 0:
                    third = third - 1
                if second == third:
                    break
                if nums[first] + nums[second] + nums[third] == 0:
                    res.append([nums[first], nums[second], nums[third]])
        return res

    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = list()

        # 枚举 a
        for first in range(n):
            # 需要和上一次枚举的数不相同
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            # c 对应的指针初始指向数组的最右端
            third = n - 1
            target = -nums[first]
            # 枚举 b
            for second in range(first + 1, n):
                # 需要和上一次枚举的数不相同
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                # 需要保证 b 的指针在 c 的指针的左侧
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                # 如果指针重合，随着 b 后续的增加
                # 就不会有满足 a+b+c=0 并且 b<c 的 c 了，可以退出循环
                if second == third:
                    break
                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])

        return ans

    def isValidBST(self, root: TreeNode) -> bool:  #https://leetcode-cn.com/problems/validate-binary-search-tree/submissions/
        inorder = self.inorder(root)
        return inorder == list(sorted(set(inorder)))

    def inorder(self, root):
        if root is None:
            return []
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)
