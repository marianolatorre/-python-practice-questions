class Solution:
    def hammingDistance(self, n1: int, n2: int) -> int:
        test = 1
        count = 0
        print(bin(n1),bin(n2))
        i = 0
        while i <= 32:
            print(n1 >> i & 1, n2 >> i & 1)
            if  n1 >> i & 1 != n2 >> i & 1:
                count += 1
            i += 1

        return count
                

s=Solution()
print(s.hammingDistance(589,61))