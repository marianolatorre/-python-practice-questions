class Solution:
    def __init__(self):
        self.cache = dict()
        
    def rob(self, nums) -> int:
        return self.robfrom(nums, 0)
    
    def robfrom(self, nums, start) -> int:
        ln = len(nums)-start
        if ln == 0:
            return 0
        elif ln == 1: 
            return nums[start]
        elif ln == 2:
            return max(nums[start],nums[start+1])
        else: 
            self.cache[start+2] = self.cache.get(start+2, self.robfrom(nums, start+2))
            self.cache[start+3] = self.cache.get(start+3, self.robfrom(nums, start+3))
           
            opt1 = nums[start] + self.cache[start+2]
            opt2 = nums[start+1] + self.cache[start+3]
            
            return max(opt1, opt2)

        
        #  [0,1,2,3,4]
        # [0] + [2,3,4]
        # [1] + [3,4]
        # [2] + [4]
s=Solution()
print(s.rob([226,174,214,16,218,48,153,131,128,17,157,142,88,43,37,157,43,221,191,68,206,23,225,82,54,118,111,46,80,49,245,63,25,194,72,80,143,55,209,18,55,122,65,66,177,101,63,201,172,130,103,225,142,46,86,185,62,138,212,192,125,77,223,188,99,228,90,25,193,211,84,239,119,234,85,83,123,120,131,203,219,10,82,35,120,180,249,106,37,169,225,54,103,55,166,124]))