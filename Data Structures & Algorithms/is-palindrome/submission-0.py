class Solution:
    def isPalindrome(self, s: str) -> bool:
        nstr = ''
        for char in s:
            if char.isalnum():
                nstr += char.lower()
        return nstr == nstr[::-1]
        