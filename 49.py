# s = ["eat","tea","tan","ate","nat","bat"]
s = [""]

split = []
for i in range(len(s)):
    split_item = [item for item in s[i]]
    split_item.sort()
    split.append(split_item)

final = []
is_in = [0]*len(s)
for i in range(len(split)):
    if is_in[i] == 1:
        continue
    if is_in[i] == 0:
        temp = [s[i]]
        for j in range(i+1, len(split)):
            if split[i] == split[j]:
                temp.append(s[j])
                is_in[j] = 1
        final.append(temp)

print(final)

import collections
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
        print(anagrams)
        return list(anagrams.values())
    
s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
