class Solution:

    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        result = nums
        for i in range(k):
            # print(result)
            result = self.rotateOnce(result)
        return result

    def rotateOnce(self, nums):
        if len(nums) < 2:
            return nums
        return nums[len(nums)-1:] + nums[:-1]
    
    def rotateInPlaceSlice(self, nums, k):
        if len(nums) < 2:
            return nums
        k = k % len(nums)
        return nums[len(nums)-k:] + nums[:-k]

    def rotateInPlace(self, nums, k):
        

s=Solution()
print(s.rotate([1,2,3,4,5,6,7],3))
print(s.rotateInPlace([1,2,3,4,5,6,7],3))

k=1
1,2,3,4,5,6,7
7,1,2,3,4,5,6
0,1,2,3,4,5,6

1,2,3,4,5,6,7 / aux=7
save=2
1,1,3,4,5,6,7 / 2

