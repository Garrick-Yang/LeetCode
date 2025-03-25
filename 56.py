from typing import List

class Solution_2:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        all_nums = [False] * 20002
        for interval in intervals:
            for i in range(interval[0]*2, interval[1]*2+1):
                all_nums[i] = True

        result = []
        start = None
        for i, num in enumerate(all_nums):
            if num == True and start is None:
                start = i
            elif num == False and start is not None:
                result.append([start//2, i//2])
                start = None
        return result
    
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        for interval in intervals:
            if len(res)==0 or res[-1][1] < interval[0]:
               res.append(interval)
            else:
                  res[-1][1] = max(res[-1][1], interval[1])
        return res

s = Solution()
print(s.merge([[1,3],[2,6],[8,10],[15,18]])) # [[1,6],[8,10],[15,18]]
