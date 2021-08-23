# -*- coding: utf-8 -*-
# Runtime: 24 ms, faster than 71.18% of Python online submissions for Rotate List.
# Memory Usage: 13.4 MB, less than 84.12% of Python online submissions for Rotate List.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def display(self):
        stack = []
        currentNode = self
        stack.append(currentNode)
        while currentNode.next != None:
            currentNode = currentNode.next
            stack.append(currentNode)
        size = len(stack)
        for i in range(size - 1):
            print(stack[i].val, " -> ", end="")
        print(stack[size - 1].val)


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # connect to a loop
        if head == None:
            return None
        curNode = head
        length = 1
        while curNode.next != None:
            curNode = curNode.next
            length += 1
        curNode.next = head
        k = length - (k % length)
        for i in range(k):
            head = head.next
            curNode = curNode.next
        curNode.next = None
        return head


def main():
    obj = Solution()
    nums = [i for i in range(10)]
    size = len(nums)
    for i in range(size):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
        print("Rotate", nums[i], "units : ", end="")
        obj.rotateRight(head, nums[i]).display()


if __name__ == '__main__':
    main()
