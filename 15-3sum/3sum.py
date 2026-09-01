class Solution:
    def two_sum(self, f, nums, res):
        i = f + 1
        j = len(nums) - 1
        while i < j:
            total = nums[f] + nums[i] + nums[j]
            if total < 0:
                i += 1
            elif total > 0:
                j -= 1
            else:
                res.append([nums[f], nums[i], nums[j]])
                i += 1
                j -= 1

                while i < j and nums[i] == nums[i - 1]:
                    i += 1
                    
                while i < j and nums[j] == nums[j + 1]:
                    j -= 1


    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []

        for f in range(len(nums) - 2):
            if nums[f] > 0:
                break
            if f > 0 and nums[f] == nums[f-1]:
                continue
            self.two_sum(f, nums, res)
        
        return res