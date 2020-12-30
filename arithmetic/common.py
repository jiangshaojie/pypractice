# -*- coding: utf-8 -*-
from typing import List
from arithmetic.util.TreeNode import TreeNode
import collections


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

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # https://leetcode-cn.com/problems/two-sum/
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return [0]

    def twoSum1(self, nums: List[int], target: int) -> List[int]:
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

    def isValidBST(self, root: TreeNode) -> bool:
        # https://leetcode-cn.com/problems/validate-binary-search-tree/submissions/
        inorder = self.inorder(root)
        return inorder == list(sorted(set(inorder)))

    def inorder(self, root):
        if root is None:
            return []
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)

    def isValidBST1(self, root: TreeNode) -> bool:
        self.prev = None
        return self.helper(root)

    def helper(self, root):
        if root is None:
            return True
        if not self.helper(root.left):
            return False
        if self.prev and self.prev.val >= root.val:
            return False
        self.prev = root
        return self.helper(root.right)

    def isValidBST2(self, root: TreeNode) -> bool:
        return self.checkBST(root, None, None)

    def checkBST(self, root, min, max):
        if root is None:
            return True
        if (min is not None and root.val <= min) or (max is not None and root.val >= max):
            return False
        return self.checkBST(root.left, min, root.val) and self.checkBST(root.right, root.val, max)

    def isValidBST3(self, root: TreeNode) -> bool:
        """
        递归写法
        :param root:
        :return:
        """

        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True
            val = node.val
            if val <= lower or val >= upper:
                return False
            if not helper(node.left, lower, val):
                return False
            if not helper(node.right, val, upper):
                return False
            return True

        return helper(root)

    def isValidBST_inorder(self, root: TreeNode) -> bool:
        """
        中序遍历
        :param root:
        :return:
        """
        stack, inorder = [], float("-inf"),
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # 如果中序便利得到的节点的值小于前一个inorder，说明不是二叉搜索树
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right
        return True

    def myPow(self, x, n):
        """
        https://leetcode-cn.com/problems/powx-n/
        :param x:
        :param n:
        :return:
        """
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n - 1)
        return self.myPow(x * x, n / 2)

    def myPow1(self, x, n):
        """

        :param x:
        :param n:
        :return:
        """
        if n < 0:
            x = 1 / x
            n = -n
        pows = 1
        while n:
            if n & 1:
                pows *= x
            x *= x
            n >>= 1
        return pows

    def majorityElement(self, nums):
        """
        https://leetcode-cn.com/problems/majority-element/ 多数元素
        majorityElement
        :return:
        """
        counts = collections.Counter(nums)
        print(counts)
        return max(counts.keys(), key=counts.get)

    def majorityElement1(self, nums):
        nums.sort()
        return nums[len(nums) // 2]

    def majorityElement2(self, nums, lo=0, hi=None):
        def majority_element_rc(lo, hi):
            if lo == hi:
                return nums[0]
            mid = (hi - lo) // 2 + lo
            left = majority_element_rc(lo, mid)
            right = majority_element_rc(mid + 1, hi)
            if left == right:
                return left
            left_count = sum(1 for i in range(lo, hi + 1) if nums[i] == left)
            right_count = sum(i for i in range(lo, hi + 1) if nums[i] == right)
            return left if left_count > right_count else right

        return majority_element_rc(0, len(nums) - 1)


if __name__ == '__main__':
    solution = Solution()
    # b = solution.myPow(2, 4)
    b = solution.majorityElement2([2, 2, 1, 1, 1, 2, 2])
    print(b)
