class Solution:
    def hammingWeight(self, n: int) -> int:
        test = 1
        count = 0
        while test <= n:
            if test & n:
                count += 1
            test = test * 2
        return count
        
