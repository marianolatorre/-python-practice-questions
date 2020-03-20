class Solution:
    def intersect(self, nums1, nums2):
        num1_rates = {}
        num2_rates = {}
        for x in nums1:
            num1_rates[x] = num1_rates.get(x,0)+1
        for x in nums2:
            num2_rates[x] = num2_rates.get(x,0)+1

        print(num1_rates)
        print(num2_rates)
        result = []
        for x in num1_rates:
            o1 = num1_rates.get(x,0)
            o2 = num2_rates.get(x,0)
            result += [x] * min(o1,o2)
        return result


s=Solution()
# print(s.intersect([1,2,3],[3,3,1,4]))
print(s.intersect([2,2],[1,2,2,1]))