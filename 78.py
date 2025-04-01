from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []  # 存放最终结果的列表
        path = []    # 存放当前正在构建的子集的列表

        def backtrack(startIndex: int):
            """
            回溯函数。

            Args:
                startIndex: 本轮选择的起始索引。
            """
            # 1. 存放结果：每个节点都代表一个子集，都要加入结果集
            #    必须添加 path 的副本，否则后续 path 的修改会影响已存入 result 的列表
            result.append(path[:]) 

            # (隐式的终止条件：当 startIndex >= len(nums) 时，下面的 for 循环不会执行，递归自然结束)
            # if startIndex >= len(nums):
            #     return 

            # 2. 单层搜索逻辑：遍历选择列表
            #    选择范围是 [startIndex, len(nums) - 1]
            for i in range(startIndex, len(nums)):
                # 3. 处理节点：做出选择
                path.append(nums[i])
                # 4. 递归：进入下一层决策树
                #    注意传入的是 i + 1，表示下一轮选择要从 i 的下一个元素开始
                backtrack(i + 1)
                # 5. 撤销处理：回溯，撤销选择
                path.pop()

        # 初始调用回溯函数，从索引 0 开始
        backtrack(0)
        return result

# 示例用法
solver = Solution()

nums1 = [1, 2, 3]
print(f"输入: nums = {nums1}")
print(f"输出: {solver.subsets(nums1)}") 
# 预期输出: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]] (顺序可能不同)

nums2 = [0]
print(f"输入: nums = {nums2}")
print(f"输出: {solver.subsets(nums2)}")
# 预期输出: [[], [0]]