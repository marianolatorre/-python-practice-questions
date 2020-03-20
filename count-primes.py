class Solution:
    def countPrimes(self, n: int) -> int:
        # print("call",n)
        if n == 3:
            return 2
        elif n==2:
            return 1
        elif n==1:
            return 0
        
        next_test = int(n/2)
        while next_test > 1:
            if n % next_test == 0:
                # print("divided ",n, next_test)
                return self.countPrimes(n-1)
            next_test -= 1
        
        # print("prime found")
        return 1 + self.countPrimes(n-1)
        
        #1,2,3,4,5,6,7,8,9,10
