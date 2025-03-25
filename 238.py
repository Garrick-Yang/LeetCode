from typing import List

class Solution_2:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left, right, ans = [0] * length, [0] * length, [0] * length

        left[0] = 1
        for i in range(1, length):
            left[i] = left[i - 1] * nums[i - 1]

        right[length - 1] = 1
        for i in reversed(range(length - 1)):
            right[i] = right[i + 1] * nums[i + 1]

        for i in range(length):
            ans[i] = left[i] * right[i]

        return ans

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = [0] * length

        ans[0] = 1
        for i in range(1, length):
            ans[i] = ans[i - 1] * nums[i - 1]

        R = 1
        for i in reversed(range(length)):
            ans[i] = ans[i] * R
            R *= nums[i]

        return ans
    

s = Solution()
nums = [1,2,3,4]
print(s.productExceptSelf(nums)) # [24,12,8,6]
