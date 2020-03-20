class Solution:
    def __init__(self):
        self.cache=dict()
        
    def climbStairs(self, n: int) -> int:
        
        if n < 3:
            return n
        elif n in self.cache:
            return self.cache[n]
        else:
            if n-1 not in self.cache:
                self.cache[n-1] = self.climbStairs(n-1)
            if n-2 not in self.cache:
                self.cache[n-2] = self.climbStairs(n-2)

            return self.cache[n-1] + self.cache[n-2]
