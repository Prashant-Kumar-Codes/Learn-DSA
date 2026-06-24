class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = 1
        seen = {}

        while left != right:
            if right == len(nums):
                right = left + 2
                left+= 1
            if nums[left] + nums[right] == target: return left, right
            right+=1
