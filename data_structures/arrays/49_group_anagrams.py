"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""
from typing import List

"""
Hash-map + signature pattern (faster on LC)

**Time Complexity**
Let N = number of strings, K = average length of a string.
For each string you compute ''.join(sorted(st)) → O(K log K).
You do this N times → O(N · K log K).
Dict insert/append is O(1) average per string.
Total: O(N · K log K).

**Space Complexity**
You create a sorted key per string of length ~K → O(N · K) extra space for keys.
The dict and lists store references to the original strings (no copies), which is O(N) overhead.
Total extra space (not counting input): O(N · K).
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sorted strings hashmap
        hm = {}
        for st in strs:
            l = ''.join(sorted(st))
            if l in hm.keys():
                hm[l].append(st)
            else:
                hm[l]=[st]
        return list(hm.values())

"""
Use a 26-count tuple as the key (frequency of 'a'..'z').
Time: O(N · K)
Space for keys: O(26N) = O(N) (better than storing sorted copies)
"""

class Solution:
    def key(self, s):
        # ord is a Python builtin that returns the Unicode code point (an integer) for a single character.
        # list to store occurence of each letter
        cnt = [0] * 26
        for ch in s:
            idx = ord(ch) - ord('a')
            cnt[idx] += 1
        # Return tuple as they are hashable, and dict keys must be hashable
        # Lists are mutable
        return tuple(cnt)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for st in strs:
            k = self.key(st)
            if k not in groups:
                groups[k] = []
            groups[k].append(st)
        return list(groups.values())
