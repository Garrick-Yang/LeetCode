from typing import List

class Solution_2:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        print(nums)

class Solution_3:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        count = 0

        for start in range(n):
            current = start
            prev = nums[start]
            while True:
                next = (current + k) % n
                nums[next], prev = prev, nums[next]
                current = next
                count += 1
                if start == current:
                    break
            if count == n:
                break
        print(nums)

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        '''
        reverse the whole list, then reverse the first k elements, then reverse the rest
        '''
        n = len(nums)
        k = k % n
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
        print(nums)


s = Solution()
nums = [1,2,3,4,5,6,7]
k = 3
s.rotate(nums, k) # [5,6,7,1,2,3,4]