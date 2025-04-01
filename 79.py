class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])
        # visited 数组用于记录当前路径中访问过的单元格
        visited = [[False for _ in range(n)] for _ in range(m)]

        # 定义回溯函数，对应模板中的 backtrack
        # 参数：当前单元格坐标 (i, j)，当前匹配到 word 的索引 k
        def backtrack(i, j, k):
            # 终止条件 1: 字符不匹配 或 越界 或 已访问
            # 注意：这里先判断 board[i][j] == word[k]
            if not (0 <= i < m and 0 <= j < n and not visited[i][j] and board[i][j] == word[k]):
                return False # 此路不通

            # 终止条件 2: 单词已经完全匹配
            if k == len(word) - 1:
                # 存放结果 (这里是直接返回 True，表示找到了)
                return True

            # 处理节点：标记当前单元格为已访问
            visited[i][j] = True

            # for (选择：本层集合中元素（上、下、左、右四个相邻单元格）)
            # 尝试四个相邻方向
            # 递归调用 backtrack(路径，选择列表)
            found = (backtrack(i + 1, j, k + 1) or  # 向下
                     backtrack(i - 1, j, k + 1) or  # 向上
                     backtrack(i, j + 1, k + 1) or  # 向右
                     backtrack(i, j - 1, k + 1))    # 向左

            # 回溯，撤销处理结果：将当前单元格标记为未访问
            visited[i][j] = False

            return found # 返回从当前节点出发是否能找到单词

        # ---- 主逻辑 ----
        # 遍历网格中的每个单元格作为起点
        for r in range(m):
            for c in range(n):
                # 只有当起点字符匹配 word[0] 时才开始搜索
                if backtrack(r, c, 0):
                    return True # 如果从任一起点找到了单词，直接返回 True

        # 遍历完所有起点都没有找到，返回 False
        return False

# 示例用法
board1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word1 = "ABCCED"
sol = Solution()
print(f"Board: {board1}, Word: '{word1}', Exists: {sol.exist(board1, word1)}") # Expected: True

board2 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word2 = "SEE"
print(f"Board: {board2}, Word: '{word2}', Exists: {sol.exist(board2, word2)}") # Expected: True

board3 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word3 = "ABCB"
print(f"Board: {board3}, Word: '{word3}', Exists: {sol.exist(board3, word3)}") # Expected: False (不允许重复使用单元格 'B')

board4 = [["a"]]
word4 = "a"
print(f"Board: {board4}, Word: '{word4}', Exists: {sol.exist(board4, word4)}") # Expected: True

from collections import Counter
class Solution:
    def exist(self, board, word):
        cnt=Counter(c for row in board for c in row)
        if not cnt>=Counter(word):
            return False
        if cnt[word[-1]]<cnt[word[0]]:
            word=word[::-1]
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]

        def backtrack(i, j, k):
            if not (0 <= i < m and 0 <= j < n and 
                    not visited[i][j] 
                    and board[i][j] == word[k]):
                return False
            if k == len(word) - 1:
                return True
            
            visited[i][j] = True

            found = (backtrack(i + 1, j, k + 1) or 
                     backtrack(i, j + 1, k + 1) or 
                     backtrack(i - 1, j, k + 1) or 
                     backtrack(i, j - 1, k + 1))
            
            # for 实现
            '''
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            found = False # 初始化 found 状态为 False

            # for (选择：本层集合中元素（上、下、左、右四个相邻单元格）)
            for dr, dc in directions:
                next_i, next_j = i + dr, j + dc

                # 递归调用 backtrack(路径，选择列表)
                if backtrack(next_i, next_j, k + 1):
                    # 如果从任何一个方向找到了单词
                    found = True
                    # 找到了就不需要再尝试其他方向了，可以提前结束循环
                    break # 跳出 for 循环
            '''
            visited[i][j] = False
            return found
        
        for r in range(m):
            for c in range(n):
                if backtrack(r, c, 0):
                    return True
                
        return False


'''
新代码中的优化点：

字符计数预检查 (Optimization 1: Early Exit based on Character Counts):

Python

cnt=Counter(c for row in board for c in row)
if not cnt>=Counter(word):
    return False
操作: 代码首先统计了整个 board 中每个字符出现的次数，然后统计了 word 中每个字符需要的次数。它检查 board 中的字符计数是否 足以 构成 word（即 board 中每个字符的出现次数都大于或等于 word 中对应字符的需要次数）。
优化效果: 如果 board 中某个字符的数量少于 word 中需要的数量，那么 word 肯定无法在 board 中构成。这种情况下，函数可以直接返回 False，避免了后续代价高昂的深度优先搜索（DFS），显著提高了效率，尤其是在 word 包含 board 中稀有或不存在的字符时。
搜索方向启发式优化 (Optimization 2: Search Direction Pruning):

Python

if cnt[word[-1]]<cnt[word[0]]:
    word=word[::-1]
操作: 代码比较了 word 的首字符和尾字符在 board 中的出现频率。如果尾字符 (word[-1]) 在 board 中出现的次数 少于 首字符 (word[0])，它就将 word 反转。
优化效果: DFS（回溯）的起点是 word 的第一个字符。如果 word 的某个端点的字符在 board 中出现的次数较少，那么从这个端点开始搜索，潜在的起始点就更少，可以更快地排除无效路径，从而可能减少搜索的总时间。这是一个启发式策略，不保证每次都更快，但在很多情况下能有效剪枝。
原地标记访问过的单元格 (Optimization 3: In-place Marking):

Python

board[i][j]='#' # 标记访问
# ... recursive calls ...
board[i][j]=ch  # 恢复/回溯
操作: 这段代码没有使用一个额外的 visited 二维布尔数组来标记访问过的单元格，而是直接 修改了输入 board。它将访问过的单元格暂时替换为一个特殊字符（如 '#'，假设它不会出现在原始 board 和 word 中），在回溯时再恢复原字符。
优化效果: 主要是 空间优化，节省了创建一个与 board 等大小的 visited 数组所需的 O(m*n) 空间。访问检查也可能略快一点（直接比较字符而不是访问另一个数组）。
注意: 这种方法有一个 副作用，它会临时修改输入 board。如果在调用 exist 函数后还需要使用原始的 board，这种修改可能会有问题。而使用 visited 数组则不会修改原始输入。
'''