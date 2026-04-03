#https://leetcode.com/problems/two-sum/

solution:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        result = []
        for i,num in enumerate(nums):
            diff = (target - num)
            if diff in seen:
                result = [seen[diff], i]
            seen[num] = i
        return result
