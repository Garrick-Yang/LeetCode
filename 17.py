from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        使用回溯法找出数字字符串能表示的所有字母组合。

        Args:
            digits: 一个仅包含数字 '2'-'9' 的字符串。

        Returns:
            一个包含所有可能字母组合的列表。
        """
        # 处理空输入
        if not digits:
            return []

        # 数字到字母的映射
        digit_map = {
            '2': "abc", '3': "def", '4': "ghi", '5': "jkl",
            '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"
        }

        result = []  # 存放最终结果
        path = []    # 存放当前组合的路径 (使用列表方便添加/删除字符)

        def backtrack(index: int):
            """
            回溯函数。

            Args:
                index: 当前处理的 digits 字符串的索引。
            """
            # 1. 终止条件：当路径长度等于数字字符串长度时，找到一个完整组合
            if index == len(digits):
                # 2. 存放结果：将字符列表 path 连接成字符串，加入结果集
                result.append("".join(path))
                return # 结束当前递归分支

            # 3. 获取当前层选择列表：当前数字对应的字母
            current_digit = digits[index]
            letters = digit_map[current_digit]

            # 4. 遍历选择列表
            for letter in letters:
                # 5. 处理节点：做出选择
                path.append(letter)
                # 6. 递归：处理下一个数字 (index + 1)
                backtrack(index + 1)
                # 7. 撤销处理：回溯
                path.pop()

        # 初始调用回溯函数，从索引 0 (第一个数字) 开始
        backtrack(0)
        return result

# 示例用法
solver = Solution()

digits1 = "23"
print(f"输入: digits = \"{digits1}\"")
print(f"输出: {solver.letterCombinations(digits1)}")
# 预期输出: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"] (顺序可能不同)

digits2 = ""
print(f"输入: digits = \"{digits2}\"")
print(f"输出: {solver.letterCombinations(digits2)}")
# 预期输出: []

digits3 = "2"
print(f"输入: digits = \"{digits3}\"")
print(f"输出: {solver.letterCombinations(digits3)}")
# 预期输出: ["a", "b", "c"]


class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []
        
        digits_map = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}

        res = []
        path = []

        def backtracking(index):
            if index == len(digits):
                res.append(''.join(path))
                return
        
            cur_digit = digits[index]
            letters = digits_map[cur_digit]

            for letter in letters:
                path.append(letter)
                backtracking(index + 1)
                path.pop()

        backtracking(0)
        return res