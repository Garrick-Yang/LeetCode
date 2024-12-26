from typing import List


class Solution_2:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i] == 0:
                j = i
                while j < len(nums):
                    if j + 1 < len(nums) and nums[j + 1] == 0:
                        end = j + 1
                    elif j + 1 == len(nums):
                        break
                    else:
                        end = j +1
                        nums[i], nums[end] = nums[end], nums[i]
                        break
                    j += 1
        print(nums)

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        left = right = 0
        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1

s = Solution()
s.moveZeroes([0,0,0,3,12])
