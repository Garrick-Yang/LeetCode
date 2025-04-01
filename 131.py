from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []  # 存放结果列表
        path = []    # 存放当前组合路径 (一个分割方案)
        n = len(s)

        # 辅助函数：判断一个字符串是否是回文串
        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]

        # 回溯函数
        # startIndex: 当前切割的起始位置
        def backtrack(startIndex: int):
            # 终止条件：如果起始位置已经等于字符串长度，说明找到了一组分割方案
            if startIndex == n:
                # 注意：需要添加 path 的拷贝，而不是 path 本身
                # 因为 path 在后续的回溯过程中会继续被修改
                result.append(path[:])
                return

            # 单层搜索过程：在 startIndex 后面的字符串中寻找回文子串
            # i 是当前尝试切割的子串的结束位置（包含）
            for i in range(startIndex, n):
                # 提取子串 s[startIndex...i]
                substring = s[startIndex : i + 1]

                # 判断这个子串是否是回文串
                if is_palindrome(substring):
                    # 处理节点：将回文子串加入当前路径
                    path.append(substring)

                    # 递归：从 i + 1 的位置继续寻找下一个回文子串
                    backtrack(i + 1)

                    # 回溯：撤销处理结果，将当前子串从路径中移除
                    # 以便尝试 s[startIndex...i+1] 或者其他可能性
                    path.pop()
                # else: # 如果不是回文串，则当前的切割方式无效，继续尝试下一个 i (剪枝)
                #     continue # 这个 continue 可以省略，因为 for 循环会自然进行

        # 初始调用回溯函数，从索引 0 开始
        backtrack(0)
        return result

# --- 测试用例 ---
sol = Solution()

# 示例 1
s1 = "aab"
print(f"输入: s = \"{s1}\"")
print(f"输出: {sol.partition(s1)}")
# 预期输出: [["a","a","b"],["aa","b"]]

# 示例 2
s2 = "a"
print(f"输入: s = \"{s2}\"")
print(f"输出: {sol.partition(s2)}")
# 预期输出: [["a"]]

# 示例 3
s3 = "racecar"
print(f"输入: s = \"{s3}\"")
print(f"输出: {sol.partition(s3)}")
# 预期输出: [["r","a","c","e","c","a","r"], ["r","a","cec","a","r"], ["r","aceca","r"], ["racecar"]]

# 示例 4 (空字符串)
s4 = ""
print(f"输入: s = \"{s4}\"")
print(f"输出: {sol.partition(s4)}")
# 预期输出: [[]]

class Solution:
    def partition(self, s):
        result = []
        path = []
        n = len(s)

        def is_palindrome(sub):
            return sub == sub[::-1]
        
        def backtrack(startIndex):
            if startIndex == n:
                result.append(path[:])
                return
            
            for i in range(startIndex, n):
                substring = s[startIndex : i + 1]
                if is_palindrome(substring):
                    path.append(substring)
                    backtrack(i + 1)
                    path.pop()

        backtrack(0)
        return result
