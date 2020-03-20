class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        i = 0
        while i <= 32:
            if  x >> i & 1 != y >> i & 1:
                count += 1
            i += 1

        return count
        
