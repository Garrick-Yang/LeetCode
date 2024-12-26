class Solution_2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if s == " ":
            return 1
        if len(s) == 1:
            return 1
        maxLen = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if j == len(s) - 1 and s[j] not in s[i:j]:
                    maxLen = max(maxLen, j - i + 1)
                if s[j] in s[i:j]:
                    maxLen = max(maxLen, j - i)
                    break
                
        return maxLen

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_set = set()
        maxLen = 0
        right = 0
        for left in range(len(s)):
            if left != 0:
                s_set.remove(s[left - 1])
            while right < len(s) and s[right] not in s_set:
                s_set.add(s[right])
                right += 1
            maxLen = max(maxLen, right - left)
        return maxLen
s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))