import re, string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        pattern = re.compile('[\W_]+')
        filter_s = pattern.sub('', s).lower()
        return filter_s == filter_s[::-1]