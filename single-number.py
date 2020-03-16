class Solution:
    def singleNumber2(self, nums) -> int:
        single=set()
        ocurrence={}
        for x in nums:
            new_ocurrence = ocurrence.get(x,0)+1
            ocurrence[x] = new_ocurrence
            if new_ocurrence == 1:
                single.add(x)
            else:
                single.discard(x)
        
        return list(single)[0]

    def singleNumber(self, nums) -> int:
        single=set()
        for x in nums:
            if x in single:
                single.remove(x)
            else:
                single.add(x)
        
        return list(single)[0]

s=Solution()
print(s.singleNumber([1,1,2,3,2,5,8,7,3,8,7]))