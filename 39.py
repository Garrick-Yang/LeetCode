from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        使用回溯法找出 candidates 中和为 target 的所有不同组合。
        candidates 中的数字可以无限制重复被选取。

        Args:
            candidates: 无重复元素的整数数组。
            target: 目标整数。

        Returns:
            一个包含所有可能组合的列表。
        """
        result = []  # 存放结果列表
        path = []    # 存放当前组合路径

        # 为了潜在的剪枝优化，可以排序，但对于本题核心逻辑非必需
        candidates.sort() 

        def backtrack(startIndex: int, current_sum: int):
            """
            回溯函数

            Args:
                startIndex: 本轮选择的起始索引（避免重复组合的关键）
                current_sum: 当前路径中元素的和
            """
            # --- 满足结束条件 ---
            # 1. 失败/剪枝: 当前和已超过目标，此路不通
            if current_sum > target:
                return
            # 2. 成功: 当前和等于目标，找到一个解
            if current_sum == target:
                result.append(path[:]) # 存放结果 (必须是 path 的副本)
                return

            # --- 单层搜索逻辑 ---
            # '选择列表' 是 candidates[startIndex] 到末尾的元素
            for i in range(startIndex, len(candidates)):
                num = candidates[i] # 当前选择的数字

                # (可选剪枝：如果 candidates 已排序)
                if num > target - current_sum:
                    break # 后面的数更大，肯定也超了

                # 做选择: 将数字加入路径
                path.append(num)

                # 递归: 探索下一层
                # 注意：因为数字可以重复使用，所以下次递归仍然从索引 i 开始
                backtrack(i, current_sum + num)

                # 撤销选择: 回溯，将数字从路径移除
                path.pop()

        # 初始调用回溯函数
        # 从索引 0 开始，初始和为 0，初始路径为空
        backtrack(0, 0)
        return result

# 示例用法
solver = Solution()

candidates1 = [2, 3, 6, 7]
target1 = 7
print(f"输入: candidates = {candidates1}, target = {target1}")
print(f"输出: {solver.combinationSum(candidates1, target1)}")
# 预期输出: [[2, 2, 3], [7]] (顺序可能不同)

candidates2 = [2, 3, 5]
target2 = 8
print(f"输入: candidates = {candidates2}, target = {target2}")
print(f"输出: {solver.combinationSum(candidates2, target2)}")
# 预期输出: [[2, 2, 2, 2], [2, 3, 3], [3, 5]] (顺序可能不同)

candidates3 = [2]
target3 = 1
print(f"输入: candidates = {candidates3}, target = {target3}")
print(f"输出: {solver.combinationSum(candidates3, target3)}")
# 预期输出: []

class Solution:
    def combinationSum(self, candidates, target):
        candidates.sort()
        result = []
        path = []

        def backtrack(startIndex, current_sum):
            if current_sum > target:
                return
            if current_sum == target:
                result.append(path[:])
            
            for i in range(startIndex, len(candidates)):
                num = candidates[i]
                if num > target - current_sum:
                    break
                path.append(num)
                backtrack(i, current_sum + num)
                path.pop()

        backtrack(0, 0)
        return result 