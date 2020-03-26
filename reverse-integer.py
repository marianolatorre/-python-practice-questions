class Solution:
    def reverse(self, x: int) -> int:
        n = str(abs(x))
        sign = 1
        if x < 0:
            sign = -1
        total = 0
        
        for i,c in enumerate(n):
            val = int(c) * pow(10,i)
            total = total + val
            
        result = total * sign
        if result > pow(2,31)-1:
            return 0
        elif result < -1 * pow(2,31):
            return 0
        else:
            return result


s=Solution()
print(s.reverse(123))
print(s.reverse(-120))
print(s.reverse(1534236469))
