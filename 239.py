from typing import List
import heapq
import collections

class Solution_2:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        lst_tupe = [(-nums[i], i) for i in range(k)]
        heapq.heapify(lst_tupe)
        res = [-lst_tupe[0][0]]
        for i in range(k, n):
            heapq.heappush(lst_tupe, (-nums[i], i))
            while lst_tupe[0][1] <= i - k:
                heapq.heappop(lst_tupe)
            res.append(-lst_tupe[0][0])
        return res
    
class Solution_3:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = collections.deque()
        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)

        ans = [nums[q[0]]]
        for i in range(k, n):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
            while q[0] <= i - k:
                q.popleft()
            ans.append(nums[q[0]])
        
        return ans
    
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        pre_max, suf_max = [0] * n, [0] * n
        for i in range(n):
            if i % k == 0:
                pre_max[i] = nums[i]
            else:
                pre_max[i] = max(pre_max[i - 1], nums[i])
        for i in range(n - 1, -1, -1):
            if (i + 1) % k == 0 or i == n - 1:
                suf_max[i] = nums[i]
            else:
                suf_max[i] = max(suf_max[i + 1], nums[i])
        res = []
        for i in range(n - k + 1):
            res.append(max(suf_max[i], pre_max[i + k - 1]))

        return res

s = Solution()
print(s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)) # [3,3,5,5,6,7]