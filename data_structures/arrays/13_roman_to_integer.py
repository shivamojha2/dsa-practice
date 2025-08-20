"""
Given a roman numeral, convert it to an integer.

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        # Time complexity = O(n), space = O(1).
        hm = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        total = 0
        prev = 0
        for idx in range(len(s)-1, -1, -1):
            val = hm[s[idx]]
            if val < prev:
                total -= val
            else:
                total += val
            prev = val
        return total
