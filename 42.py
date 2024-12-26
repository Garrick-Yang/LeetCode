from typing import List

'''
1. 
左右指针从两端向中间移动，想要正确计算储水量需要知道本端的最高点高度，以及确保对方有一个不低于本端最高点的柱子。 
左右两端轮流占领目前遍历到的最高点，当一方占据着全局最高点时。
另一方前进，直到遇到了一个比全局最高点更高的点，换另一方前进，循环往复直到 left, right 碰面。
可移动的一方每步更新自己这侧的最高点，由于另一方此时占据着全局最高点，
所以可以保证另一方有一个不低于本方最高点的柱子，也就确保了当前对储水量的计算是正确的.
2.
对于height[left] < height[right]，则必有 leftMax < rightMax 的理解
从最开始进行模拟，如果left高度小于right高度，则left右移，更高的right位置不变，假设下一轮left更高，则right会向左移，left保持在高柱子位置不变。
所以这个过程中，left和right中总是有一个停留的位置是当前已遍历过列中最高的柱子
当 height[left] < height[right] 时，上一轮移动有两种可能的情况：
一种是 height[left - 1] < height[right]，所以left右移，那么结合此轮的新比较，可知，当前right所在柱子仍然是已遍历列中的最高。
另一种是 height[left] > height[right + 1]，left是上一轮已遍历列中最高，此时right左移一位，但是此轮比较结果表明，新的right比上一轮的最高left还高，此时新right为已遍历中最高。
所以 leftMax < rightMax, height[left] < height[right], height[left] < rightMax, leftMax < height[right], 不论你怎么填这行条件，都能通过。
总结一下就是：不含已遍历中最高柱子的一侧才会移动，所以小于号右侧，即right要么已经是上一轮的已遍历最高，要么是新发现的已遍历最高（这种情况left必是上一轮的已遍历最高，只需要和它比即可，同时height[left]就是leftMax）
'''
class Solution_2:
    def trap(self, height: List[int]) -> int:
        ans = 0
        left, right = 0, len(height) - 1
        leftMax = rightMax = 0

        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])
            # if height[left] < height[right]:
            if leftMax < rightMax:
                ans += leftMax - height[left]
                left += 1
            else:
                ans += rightMax - height[right]
                right -= 1
        
        return ans

class Solution:
    def trap(self, height: List[int]) -> int:
        # 最高点的索引
        maxIndex = height.index(max(height))
        # 从左到最高点的储水量
        maxLeft = 0
        ans = 0
        for i in range(maxIndex):
            if height[i] > maxLeft:
                maxLeft = height[i]
            else:
                ans += maxLeft - height[i]
        # 从右到最高点的储水量
        maxRight = 0
        for i in range(len(height) - 1, maxIndex, -1):
            if height[i] > maxRight:
                maxRight = height[i]
            else:
                ans += maxRight - height[i]
        return ans

s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1])) # 6