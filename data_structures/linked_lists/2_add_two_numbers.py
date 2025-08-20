"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
"""
from typing import Optional
from linked_lists.linked_list import ListNode

## Approach
## Intuition:
## - We need to add the two numbers digit by digit.
## - We need to handle the carry.
## - We need to return the result as a linked list.
## - We need to handle the case where the two numbers have different lengths.
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        carry = 0
        while l1 or l2 or carry:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            total = a+b+carry
            digit = total%10
            carry = total//10
            tail.next = ListNode(digit)
            tail = tail.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next
