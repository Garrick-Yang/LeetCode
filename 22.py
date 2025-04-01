from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []  # 存放结果列表
        # path = [] # 我们用 current_string 代替路径

        # 参数: current_string (当前路径), open_count (已用左括号数), close_count (已用右括号数)
        def backtrack(current_string, open_count, close_count):
            # 终止条件: 字符串长度达到 2*n
            if len(current_string) == 2 * n:
                result.append(current_string) # 存放结果
                return

            # for (选择：本层集合中元素)
            # 选择 1: 添加左括号 '('
            if open_count < n:
                # 处理节点: 将 '(' 添加到当前字符串
                # backtrack(路径，选择列表); // 递归
                backtrack(current_string + '(', open_count + 1, close_count)
                # 回溯: 由于字符串不可变性，这里是隐式回溯，无需显式操作

            # 选择 2: 添加右括号 ')'
            if close_count < open_count: # 必须满足右括号数小于左括号数
                # 处理节点: 将 ')' 添加到当前字符串
                # backtrack(路径，选择列表); // 递归
                backtrack(current_string + ')', open_count, close_count + 1)
                # 回溯: 隐式回溯

        # 初始调用回溯函数
        backtrack("", 0, 0)
        return result

# 示例用法
solver = Solution()
n = 3
output = solver.generateParenthesis(n)
print(f"对于 n = {n}, 所有可能的有效括号组合是:")
print(output)
# 预期输出: ["((()))","(()())","(())()","()(())","()()()"]

n = 1
output = solver.generateParenthesis(n)
print(f"对于 n = {n}, 所有可能的有效括号组合是:")
print(output)
# 预期输出: ["()"]

class Solution:
    def generateParenthesis(self, n):
        result = []

        def backtrack(current_string, open_count, close_count):
            if len(current_string) == n * 2:
                result.append(current_string)
                return

            if open_count < n:
                backtrack(current_string + '(', open_count + 1, close_count)

            if close_count < open_count:
                backtrack(current_string + ')', open_count, close_count + 1)

        backtrack("", 0, 0)
        return result