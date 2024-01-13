from typing import List
from bisect import bisect_left

# class Solution:
#     def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
#         for i, interval in enumerate(intervals):
#             interval.append(i)
#         intervals.sort()
#
#         n = len(intervals)
#         ans = [-1] * n
#         for _, end, id in intervals:
#             i = bisect_left(intervals, [end])
#             if i < n:
#                 ans[id] = intervals[i][2]
#         return ans
# # findRightInterval([[3,4],[2,3],[1,2]])
# a = Solution()
# print(a.findRightInterval([[3,4],[2,3],[1,2]]))

#
intervals = [[1,2,2],[2,3,1],[3,4,0]]
end = 2
i = bisect_left(intervals, [end])
print(i)