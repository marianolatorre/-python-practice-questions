class Solution:
    def reverseBits(self, n: int) -> int:
        x = 32 # 64
        total = 0
        
        for i in range(x):
            index = x-1-i
            bit = n >> i & 1
            total += pow(2,index) * bit
            
        return total
        
        
        
        
