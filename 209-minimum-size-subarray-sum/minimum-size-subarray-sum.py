class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        i = summ = 0
        length = float('inf')

        for j in range(len(nums)):
            summ += nums[j]
            while summ >= target:
                length = min(length, (j-i+1))
                summ -= nums[i]
                i += 1

        return 0 if length == float('inf') else length


