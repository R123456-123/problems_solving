class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        if n == 1:
            return nums[0]

        dp1 = nums[0]
        dp2 = max(nums[0],nums[1])

        if n == 2:
            return dp2

        for i in range(2, n):
            cur = max(dp1 + nums[i], dp2)
            dp1 = dp2
            dp2 = cur

        return dp2





        