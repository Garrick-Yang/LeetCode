from typing import List

class Solution_2:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak
    

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums ==[]:
            return 0
        # nums = list(set(nums))
        num_set = set(nums) # list会超时
        max_consecutive = 0
        for num in nums:
            if num - 1 not in nums:
                start = num
                consecutive = 1

                while start + 1 in nums:
                    start += 1
                    consecutive += 1

                max_consecutive = max(max_consecutive, consecutive)

        return max_consecutive

s = Solution()
print(s.longestConsecutive([0,-1]))