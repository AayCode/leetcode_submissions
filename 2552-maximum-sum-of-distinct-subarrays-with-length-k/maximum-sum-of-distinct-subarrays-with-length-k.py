class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        # i = window_sum = max_sum = 0
        # seen = set()

        # for j in range(len(nums)):
        #     while nums[j] in seen:
        #         window_sum -= nums[i]
        #         seen.remove(nums[i])
        #         i += 1

        #     window_sum += nums[j]
        #     seen.add(nums[j])
     
        #     if len(seen) == k:
        #         max_sum = max(window_sum, max_sum)
        #         window_sum -= nums[i]
        #         seen.remove(nums[i])
        #         i += 1
                

        # return max_sum

        i = 0
        summ = maxx = dups = 0
        seen = {}

        for j in range(k):
            summ += nums[j]
            if nums[j] not in seen:
                seen[nums[j]] = 0
            seen[nums[j]] += 1

            if seen[nums[j]] > 1:
                dups += 1

        if dups == 0:
            maxx = max(summ, maxx)

        for j in range(k, len(nums)):
            summ += nums[j]
            if nums[j] not in seen:
                seen[nums[j]] = 0
            seen[nums[j]] += 1

            if seen[nums[j]] > 1:
                dups += 1

            summ -= nums[i]
            if seen[nums[i]] > 1:
                dups -= 1
            seen[nums[i]] -= 1
            i += 1

            if dups == 0:
                maxx = max(summ, maxx)

        return maxx







        