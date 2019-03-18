# coding=utf-8
# python3
# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        # initialization
        result = ListNode(0)
        p = result
        carry = 0
        # same add
        while l1 and l2:
            sum = l1.val + l2.val + carry
            # carry flag
            carry = 0
            if sum >= 10:
                sum -= 10
                carry = 1
            p.next = ListNode(sum)
            l1 = l1.next
            l2 = l2.next
            p = p.next
        # l1 more than l2 length
        if l1:
            while l1:
                sum = l1.val + carry
                carry = 0
                if sum >= 10:
                    sum -= 10
                    carry = 1
                p.next = ListNode(sum)
                l1 = l1.next
                p = p.next
        # l2 more than l1 length
        if l2:
            while l2:
                sum = l2.val + carry
                carry = 0
                if sum >= 10:
                    sum -= 10
                    carry = 1
                p.next = ListNode(sum)
                l2 = l2.next
                p = p.next
        # clean the carry
        if carry:
            p.next = ListNode(carry)
            p = p.next
        return result.next