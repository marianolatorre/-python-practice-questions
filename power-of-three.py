class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        
        current = 1
        while current <= n:
            if current == n:
                return True
            else:
                current = current * 3
        
        return False
