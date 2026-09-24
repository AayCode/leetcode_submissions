class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        i = 0
        summ = 0
        length = float('inf')
        n = len(nums)

        for j in range(n):
            summ += nums[j]
            while summ >= target:
                length = min(length, (j-i+1))
                summ -= nums[i]
                i += 1

        return 0 if length == float('inf') else length


