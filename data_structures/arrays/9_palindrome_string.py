"""
Given an integer x, return true if x is a palindrome, and false otherwise.
 
Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Follow up: Could you solve it without converting the integer to a string?
"""
## Aproach 1
## Convert to string and then list and then loop through the list to check if the string is a palindrome. Break if any character is not the same.
class Solution:
    def isPalindrome(self, x: int) -> bool:
        "O(d) time, O(d) extra space."
        l = list(str(x))
        flg = True
        for i in range(0, len(l)//2):
            if l[i] != l[-(i+1)]:
                flg = False
                break
        return flg
    
# Approach 2 - without converting to string
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        rev = 0
        temp = x
        while temp > 0:
            rev = rev * 10 + temp % 10
            temp = temp // 10
        return rev == x

## Approach 3 (no string, safer than full reverse): reverse only half the number.
class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Early rejects: x < 0 and "ends with 0 but not 0"
        Loop: while temp > rev: reverses only half
        Return: temp == rev (even) or temp == rev // 10 (odd)

        Time: O(d) where d = number of digits
        Space: O(1).
        """
        if x % 10 == 0 and x != 0:
            return False
        if x < 0:
            return False
        rev = 0
        temp = x
        while temp > rev:
            rev = rev*10 + temp%10
            temp //= 10
        return temp == rev or temp == rev // 10
