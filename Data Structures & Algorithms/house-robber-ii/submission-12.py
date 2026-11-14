class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])

        return max(self.helper(nums, 0, len(nums) - 1), self.helper(nums, 1, len(nums)))

    def helper(self, nums: List[int], left: int, right: int):

        dp1, dp2 = 0, 0

        for i in range(left, right):
            dp1, dp2 = dp2, max(dp1 + nums[i], dp2)

        return dp2
        
        