class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        val = ""
        max= int(len(s)/2+2)
        for i in range(0,max):
            x = s[i]
            to = len(s)-1-i
            val= s[to]
            s[to]=x
            s[i]=val
        print(s)


s=Solution()
s.reverseString(["h","e","l","l","o"])