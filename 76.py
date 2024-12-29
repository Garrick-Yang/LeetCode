from typing import List
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans_left, ans_right = -1, len(s)
        count_s = Counter()
        count_t = Counter(t)
        left = 0
        for right, char in enumerate(s):
            count_s[char] += 1
            while all(count_s[c] >= count_t[c] for c in count_t):
                if right - left < ans_right - ans_left:
                    ans_left, ans_right = left, right
                count_s[s[left]] -= 1
                left += 1
        return s[ans_left:ans_right + 1] if ans_left != -1 else ""
    
# Test
s = Solution()
print(s.minWindow("ADOBECODEBANC", "ABC")) # "BANC"

