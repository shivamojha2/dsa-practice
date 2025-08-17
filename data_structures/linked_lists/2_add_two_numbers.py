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

## Approach - O(n) time, O(1) space.
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        r = ListNode(0)
        r_tail = r
        c = 0
                
        while l1 or l2 or c:            
            v1  = (l1.val if l1 else 0)
            v2  = (l2.val if l2 else 0)

            c, out = divmod(v1 + v2 + c, 10)    
                      
            r_tail.next = ListNode(out)
            r_tail = r_tail.next                      
            
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
               
        return r.next
