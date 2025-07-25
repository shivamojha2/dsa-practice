# Given an integer x, return true if x is palindrome integer.

# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is palindrome while 123 is not.

class Solution:
    def isPalindrome(self, x):
        if x<0:
            pld_flg = False
        else:
            l = list(str(x))
            print(l)
            pld = ''
            for i in range(len(l)-1,-1,-1):
                pld = pld + l[i]
            if pld == str(x):
                pld_flg = True
            else:
                pld_flg = False
        return pld_flg

ans = Solution()  
print(ans.isPalindrome(11311))