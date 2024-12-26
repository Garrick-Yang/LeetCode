from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(p)
        ans = []
        for left in range(len(s)):
            p_set = [c for c in p]
            right = left + n
            if right > len(s):
                break
            for i in range(left, right):
                if s[i] in p_set:
                    p_set.remove(s[i])
                else:
                    break
            if len(p_set) == 0:
                ans.append(left)
        return ans
    
s = Solution()
print(s.findAnagrams("ababababab", "aab")) # [0, 6]