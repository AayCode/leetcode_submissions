class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for num in nums:
            if num != nums[k]:
                k += 1
                nums[k] = num
        return k+1        










        # k = 0
        # for num in nums:
        #     if num != nums[k]:
        #         k += 1
        #         nums[k] = num
        
        # return k+1









        # k = 0
        # for i in range(0, len(nums), 1):
        #     if nums[i] != nums[k]:
        #         k += 1
        #         nums[k] = nums[i]

        # return k+1