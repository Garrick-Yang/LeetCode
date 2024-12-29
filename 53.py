from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre_max = [0] * len(nums)
        pre_max[0] = nums[0]
        for i in range(1, len(nums)):
            pre_max[i] = max(pre_max[i-1] + nums[i], nums[i])
        return max(pre_max)
    
s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) # 6
