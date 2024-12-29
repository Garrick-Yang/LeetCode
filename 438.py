from typing import List

class Solution_2():
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
    
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len = len(s)
        p_len = len(p)

        if s_len < p_len:
            return []
        
        p_count = [0] * 26
        s_count = [0] * 26

        for i in range(p_len):
            p_count[ord(p[i]) - ord('a')] += 1
            s_count[ord(s[i]) - ord('a')] += 1

        ans = []
        if p_count == s_count:
            ans.append(0)

        for i in range(s_len - p_len):
            s_count[ord(s[i]) - ord('a')] -= 1
            s_count[ord(s[i + p_len]) - ord('a')] += 1
            if p_count == s_count:
                ans.append(i + 1)

        return ans


s = Solution()
print(s.findAnagrams("ababababab", "aab")) # [0, 6]