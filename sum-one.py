class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        for i in range(len(digits)-1, -1,-1):
            result = digits[i]+1
            digits[i]= result % 10
            if result > 9:
                if i == 0:
                    return [1] + digits
            else:
                return digits
        
        
        
s=Solution()
print(s.plusOne([9]))