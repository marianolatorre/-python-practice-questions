class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        passing = 0
        for i in len(digits)-1..0:
            result = digits[i]+1+passing
            digits[i]= result % 10
            if result > 9:
                passing = 1
                if i == 0:
                    print("no")
                    return [1] + digits
            else:
                return digits
        
s=Solution()
print(s.plusOne([9]))