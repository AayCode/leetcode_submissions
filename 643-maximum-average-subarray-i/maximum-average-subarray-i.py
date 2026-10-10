class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        res_max = float('-inf')
        summ = 0
        for i in range(k):
            summ += nums[i]

        if summ > res_max:
            res_max = summ

        for i in range(k, len(nums)):
            summ += nums[i]
            summ -= nums[i-k]

            if summ > res_max:
                res_max = summ

        return res_max/k

        