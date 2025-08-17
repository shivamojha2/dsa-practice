"""
Two sum:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Intuition:
- We use a hashmap to store the numbers and their indices.
- We iterate through the array and for each number, we check if the complement (target - nums[i]) is in the hashmap.
- If it is, we return the indices of the two numbers.
- If it is not, we add the number and its index to the hashmap.

**Q. Time/space complexity? Why “average” O(1)?**
- Hash lookups are average O(1) but worst-case O(n) with collisions. Space O(n).

**Q. Can you do it with less extra space?**
- Sorted + two pointers: O(n log n) time (to sort), O(1) extra space, but keep original indices by sorting pairs (val, idx).

**Q. If the input is already sorted?**
- Two pointers from ends → O(n), O(1) space.

**Q. How do you avoid reusing the same element?**
- Check complement before inserting current element. That ensures the pair uses a previous index.
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        hm = {}
        for i in range(l):
            c = target - nums[i]
            if c in hm:
                return [i, hm[c]]
            hm[nums[i]] = i
        return []
