class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        i = 0
        seen = set() # 1 2 3
        n = len(nums)

        # if k >= n:
        #     for j in range(n):
        #         if nums[j] in seen:
        #             return True
        #         seen.add(nums[j])
        # else:
        #     for j in range(k+1):
        #         if k == 0:
        #             return False
        #         if nums[j] in seen:
        #             return True
        #         seen.add(nums[j])

        # # 1 2 3 1 2 3
        # #       i
        # #           j

        #     for j in range(k+1, len(nums)):
        #         seen.remove(nums[i])
        #         i += 1
        #         if nums[j] in seen:
        #             return True
        #         seen.add(nums[j])
     
        # return False

        for j in range(n):
            if k == 0:
                return False
            if nums[j] in seen:
                return True
            seen.add(nums[j])

            if j - i >= k:
                seen.remove(nums[i])
                i += 1

        return False

