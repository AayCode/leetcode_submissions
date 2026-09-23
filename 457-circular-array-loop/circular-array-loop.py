class Solution:
    def nextIndex(self, nums, n, i):
        i = (i + nums[i]) % n
        return i

    def directionCheck(self, nums, n, i):
        if i == self.nextIndex(nums, n, i):
            return False
        if nums[i] >= 0 and nums[self.nextIndex(nums, n, i)] >= 0:
            return True
        elif nums[i] < 0 and nums[self.nextIndex(nums, n, i)] <= 0:
            return True
        else:
            return False
        

    def circularArrayLoop(self, nums: list[int]) -> bool:
        n = len(nums)
        for i in range(len(nums)):
            lookup = set()
            temp = i
            while True:
                if temp in lookup:
                    return True
                if self.directionCheck(nums, n, temp):
                    lookup.add(temp)
                    temp = self.nextIndex(nums, n, temp)
                else:
                    break

        return False
            

                
                
                


        

        