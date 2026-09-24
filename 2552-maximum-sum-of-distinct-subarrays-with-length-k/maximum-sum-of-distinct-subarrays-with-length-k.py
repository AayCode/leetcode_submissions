class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        i = window_sum = max_sum = 0
        seen = set()

        for j in range(len(nums)):
            while nums[j] in seen:
                window_sum -= nums[i]
                seen.remove(nums[i])
                i += 1

            window_sum += nums[j]
            seen.add(nums[j])
     
            if len(seen) == k:
                max_sum = max(window_sum, max_sum)
                window_sum -= nums[i]
                seen.remove(nums[i])
                i += 1
                

        return max_sum


        