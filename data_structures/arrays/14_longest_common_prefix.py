"""
Find the longest prefix shared by all strings; if none, return "".

["flower","flow","flight"] → "fl"
["dog","racecar","car"] → ""
[""] → ""
"""
from typing import List

## Approach - Prefix shrinking; O(n·m) time, O(1) space.
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
