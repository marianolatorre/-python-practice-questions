class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        count = 0
        for i,x in enumerate(nums):
            if x != 0:
                self.swapElem(nums, count, i)
                count += 1
        
    def swapElem(self, nums, i, j):
        nums[i], nums[j] = nums[j],nums[i]