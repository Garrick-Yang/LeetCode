class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(first = 0):
            # 所有数都填完了
            if first == n:  
                res.append(nums[:])
            for i in range(first, n):
                # 动态维护数组
                nums[first], nums[i] = nums[i], nums[first]
                # 继续递归填下一个数
                backtrack(first + 1)
                # 撤销操作
                nums[first], nums[i] = nums[i], nums[first]
        
        n = len(nums)
        res = []
        backtrack()
        return res

class Solution:
    def permute(self, nums):
        if len(nums) <=1:
            return [nums]

        ans = []
        for i in range(len(nums)):
            curr = nums[i]
            remain = nums[:i] + nums[i+1:]
            all = self.permute(remain)
            for j in all:
                ans.append([curr] + j)

        return ans

# test  
nums = [1,2,3]
s = Solution()
print(s.permute(nums))