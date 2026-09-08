"""
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]


what can we do now there are different strings but their orders are different so we have to bring together the same letters words together. first we count individual letters if the total letters of different strings matches we put them togeether and using for loop we check if they have the same characters or not. how to do that
Example 2:

Input: strs = ["x"]

Output: [["x"]]
Example 3:

Input: strs = [""]

Output: [[""]]
Constraints:

1 <= strs.length <= 10000.
0 <= strs[i].length <= 100
strs[i] is made up of lowercase English letters.

"""
from collections import Counter
class Solution:
    def groupAnagrams(self, strs):
        storage = {}
        for i in strs:
           count= Counter(i)
           key = tuple(sorted(count.items()))

           if key not in storage:
               storage[key]=[]

           storage[key].append(i)
        return list(storage.values())
            





        