class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I":1,
                 "V":5,
                 "X":10,
                 "L":50,
                 "C":100,
                 "D":500,
                 "M":1000
                }
        print(roman)

        prev = 0
        total = 0

        for c in s:
            print(c)
            current = roman.get(c,0)
            if prev == 0:
                prev = current
            elif current <= prev:
                total += prev
                prev = current
            else:
                total += current - prev
                prev = 0 
        
        return total + prev

s=Solution()
print(s.romanToInt("MCMXCIV"))