class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ls = len(s)

        if ls != len(t):
            return False

        s_rate = dict()
        t_rate = dict()

        for i in range(ls):
            s_rate[s[i]] = s_rate.get(s[i],0) + 1
            t_rate[t[i]] = t_rate.get(t[i],0) + 1
        
        for c in s:
            if s_rate.get(c,0) != t_rate.get(c,0):
                return False
        
        return True




