# -*- coding: UTF-8 -*-
import json
from copy import copy

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        # self.__str__(self.val)


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur, prev = head, None
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
            # temp=copy(cur)
            # cur.next = prev
            # prev = cur
            # cur = temp.next
        return prev

    def swapPairs(self, head: ListNode) -> ListNode:
        prev=ListNode(None)
        if head is None or head.next is None:
            return head
        oneNode,secondNode=head,head.next
        prev.next=oneNode
        while oneNode.next:
            # oneNode.next,secondNode.next,oneNode=secondNode.next,oneNode,secondNode.next
            oneNode.next,secondNode.next,prev.next,oneNode,secondNode=secondNode.next,oneNode,oneNode,oneNode.next.next,secondNode.next.next
        return prev


def stringToIntegerList(input):
    print("input: ", input)
    return json.loads(input)


def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            head = stringToListNode(line);

            ret = Solution().reverseList(head)

            out = listNodeToString(ret);
            print(out)
        except StopIteration:
            break


def main1():
    s = "[1,2,3,4,5]"
    head = stringToListNode(s);

    # ret = Solution().reverseList(head)
    ret = Solution().swapPairs(head)
    out = listNodeToString(ret);
    print(out)


if __name__ == '__main__':
    main1()
